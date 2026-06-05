"""
Multilogin X Local API — production-style Python client.

Environment:
  MULTILOGIN_BASE_URL   default http://127.0.0.1:35000
  MULTILOGIN_TOKEN      required Bearer token
"""

from __future__ import annotations

import logging
import os
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Any, Generator

import requests

logger = logging.getLogger(__name__)

PROFILE_LIST_KEYS = ("profiles", "data", "value", "items")
CDP_KEYS = (
    "cdpUrl",
    "cdp_url",
    "debuggerUrl",
    "debugger_url",
    "wsEndpoint",
    "webSocketDebuggerUrl",
)
PORT_KEYS = ("port", "debugPort", "debug_port", "seleniumPort")


class MultiloginError(Exception):
    """Local API error or unreachable agent."""

    def __init__(self, message: str, status_code: int | None = None, body: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.body = body


@dataclass
class ProfileInfo:
    """Normalized profile row from list_profiles()."""

    id: str
    name: str = ""
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_api(cls, row: dict[str, Any]) -> ProfileInfo:
        pid = str(
            row.get("id")
            or row.get("profileId")
            or row.get("uuid")
            or row.get("profile_id")
            or ""
        )
        name = str(row.get("name") or row.get("profileName") or row.get("title") or "")
        return cls(id=pid, name=name, raw=row)


@dataclass
class ProfileSession:
    """Result of start_profile() with parsed connection hints."""

    profile_id: str
    response: dict[str, Any]
    cdp_url: str | None = None
    debug_port: int | None = None

    @property
    def selenium_address(self) -> str | None:
        if self.debug_port:
            return f"127.0.0.1:{self.debug_port}"
        return None


class MultiloginClient:
    """HTTP client for Multilogin X Local API (localhost)."""

    def __init__(
        self,
        token: str | None = None,
        base_url: str | None = None,
        timeout: int = 120,
        session: requests.Session | None = None,
    ):
        self.base_url = (
            base_url or os.environ.get("MULTILOGIN_BASE_URL", "http://127.0.0.1:35000")
        ).rstrip("/")
        self.token = token or os.environ.get("MULTILOGIN_TOKEN", "")
        self.timeout = timeout
        self._session = session or requests.Session()

        if not self.token:
            raise MultiloginError("MULTILOGIN_TOKEN is not set")

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
        }

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        url = f"{self.base_url}{path}"
        timeout = kwargs.pop("timeout", self.timeout)
        try:
            response = self._session.request(
                method,
                url,
                headers=self._headers(),
                timeout=timeout,
                **kwargs,
            )
        except requests.ConnectionError as exc:
            raise MultiloginError(
                f"Cannot reach Multilogin agent at {self.base_url}. "
                "Is Multilogin X running and logged in?"
            ) from exc
        except requests.Timeout as exc:
            raise MultiloginError(f"Request timed out after {timeout}s: {method} {path}") from exc

        if not response.ok:
            raise MultiloginError(
                f"API {response.status_code} {method} {path}: {response.text[:800]}",
                status_code=response.status_code,
                body=response.text,
            )

        if not response.content:
            return {}
        try:
            return response.json()
        except ValueError:
            return {"raw": response.text}

    def ping(self) -> bool:
        """Return True if the local agent responds."""
        try:
            self._request("GET", "/api/v2/profile", timeout=10)
            return True
        except MultiloginError:
            return False

    def list_profiles(self) -> list[dict[str, Any]]:
        data = self._request("GET", "/api/v2/profile", timeout=30)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            for key in PROFILE_LIST_KEYS:
                if key in data and isinstance(data[key], list):
                    return data[key]
            if data.get("id") or data.get("profileId"):
                return [data]
        return []

    def list_profiles_normalized(self) -> list[ProfileInfo]:
        return [ProfileInfo.from_api(p) for p in self.list_profiles() if isinstance(p, dict)]

    def get_profile_id_by_name(self, name: str, *, exact: bool = True) -> str | None:
        name_cmp = name.strip().lower()
        for p in self.list_profiles_normalized():
            pn = p.name.lower()
            if (exact and pn == name_cmp) or (not exact and name_cmp in pn):
                return p.id or None
        return None

    def start_profile(self, profile_id: str) -> dict[str, Any]:
        logger.info("Starting profile %s", profile_id)
        return self._request(
            "GET",
            "/api/v2/profile/start",
            params={"profileId": profile_id},
            timeout=self.timeout,
        )

    def stop_profile(self, profile_id: str) -> dict[str, Any]:
        logger.info("Stopping profile %s", profile_id)
        return self._request(
            "GET",
            "/api/v2/profile/stop",
            params={"profileId": profile_id},
            timeout=30,
        )

    def start_profile_session(self, profile_id: str) -> ProfileSession:
        resp = self.start_profile(profile_id)
        port = self._extract_port(resp)
        return ProfileSession(
            profile_id=profile_id,
            response=resp,
            cdp_url=self.extract_cdp_url(resp),
            debug_port=port,
        )

    @contextmanager
    def profile(self, profile_id: str) -> Generator[ProfileSession, None, None]:
        """Context manager: start on enter, stop on exit (even on exception)."""
        session = self.start_profile_session(profile_id)
        try:
            yield session
        finally:
            try:
                self.stop_profile(profile_id)
            except MultiloginError as exc:
                logger.warning("Stop failed for %s: %s", profile_id, exc)

    def batch_stop(self, profile_ids: list[str], *, delay_sec: float = 0.5) -> dict[str, str]:
        results: dict[str, str] = {}
        for pid in profile_ids:
            try:
                self.stop_profile(pid)
                results[pid] = "ok"
            except MultiloginError as exc:
                results[pid] = str(exc)
            if delay_sec:
                time.sleep(delay_sec)
        return results

    def extract_cdp_url(self, start_response: dict[str, Any]) -> str | None:
        for key in CDP_KEYS:
            if start_response.get(key):
                return str(start_response[key])
        port = self._extract_port(start_response)
        if port:
            return f"http://127.0.0.1:{port}"
        return None

    def _extract_port(self, data: dict[str, Any]) -> int | None:
        for key in PORT_KEYS:
            val = data.get(key)
            if val is not None:
                try:
                    return int(val)
                except (TypeError, ValueError):
                    pass
        return None

    def close(self) -> None:
        self._session.close()

    def __enter__(self) -> MultiloginClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
