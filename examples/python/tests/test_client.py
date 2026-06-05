"""Unit tests with mocked HTTP — no Multilogin agent required."""

import os
import unittest
from unittest.mock import MagicMock, patch

# Allow import from parent package dir
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from multilogin_client import MultiloginClient, MultiloginError, ProfileInfo


class TestMultiloginClient(unittest.TestCase):
    def setUp(self) -> None:
        os.environ["MULTILOGIN_TOKEN"] = "test-token"

    def test_list_profiles_array(self) -> None:
        mock_resp = MagicMock(ok=True, content=b"[{\"id\":\"a\",\"name\":\"Test\"}]")
        mock_resp.json.return_value = [{"id": "a", "name": "Test"}]

        with patch.object(MultiloginClient, "_request", return_value=[{"id": "a", "name": "Test"}]):
            client = MultiloginClient()
            rows = client.list_profiles()
            self.assertEqual(len(rows), 1)

    def test_list_profiles_wrapped(self) -> None:
        with patch.object(
            MultiloginClient,
            "_request",
            return_value={"profiles": [{"id": "x", "profileName": "P1"}]},
        ):
            client = MultiloginClient()
            self.assertEqual(len(client.list_profiles()), 1)

    def test_extract_cdp_port(self) -> None:
        client = MultiloginClient()
        url = client.extract_cdp_url({"port": 9222})
        self.assertEqual(url, "http://127.0.0.1:9222")

    def test_profile_info(self) -> None:
        info = ProfileInfo.from_api({"profileId": "uuid-1", "profileName": "Shop US"})
        self.assertEqual(info.id, "uuid-1")
        self.assertEqual(info.name, "Shop US")

    def test_ping_false_on_error(self) -> None:
        with patch.object(MultiloginClient, "_request", side_effect=MultiloginError("down")):
            client = MultiloginClient()
            self.assertFalse(client.ping())

    def test_get_profile_id_by_name(self) -> None:
        with patch.object(
            MultiloginClient,
            "list_profiles_normalized",
            return_value=[
                ProfileInfo(id="id-1", name="Amazon US"),
                ProfileInfo(id="id-2", name="eBay UK"),
            ],
        ):
            client = MultiloginClient()
            self.assertEqual(client.get_profile_id_by_name("Amazon US"), "id-1")
            self.assertEqual(client.get_profile_id_by_name("ebay", exact=False), "id-2")


if __name__ == "__main__":
    unittest.main()
