/**
 * Minimal Multilogin X Local API client (Node 18+, native fetch).
 */

const BASE_URL = (process.env.MULTILOGIN_BASE_URL || "http://127.0.0.1:35000").replace(/\/$/, "");
const TOKEN = process.env.MULTILOGIN_TOKEN || "";

export class MultiloginClient {
  constructor(opts = {}) {
    this.baseUrl = (opts.baseUrl || BASE_URL).replace(/\/$/, "");
    this.token = opts.token || TOKEN;
    this.timeoutMs = opts.timeoutMs ?? 120_000;
    if (!this.token) throw new Error("MULTILOGIN_TOKEN is not set");
  }

  headers() {
    return {
      Authorization: `Bearer ${this.token}`,
      Accept: "application/json",
    };
  }

  async request(method, path, { params, timeoutMs } = {}) {
    const url = new URL(path, this.baseUrl);
    if (params) {
      Object.entries(params).forEach(([k, v]) => url.searchParams.set(k, v));
    }
    const controller = new AbortController();
    const t = setTimeout(() => controller.abort(), timeoutMs ?? this.timeoutMs);

    let res;
    try {
      res = await fetch(url, { method, headers: this.headers(), signal: controller.signal });
    } catch (err) {
      clearTimeout(t);
      if (err.name === "AbortError") throw new Error(`Timeout ${method} ${path}`);
      throw new Error(`Cannot reach agent at ${this.baseUrl}. Is Multilogin X running?`);
    }
    clearTimeout(t);

    const text = await res.text();
    if (!res.ok) throw new Error(`API ${res.status}: ${text.slice(0, 500)}`);
    if (!text) return {};
    try {
      return JSON.parse(text);
    } catch {
      return { raw: text };
    }
  }

  async listProfiles() {
    const data = await this.request("GET", "/api/v2/profile", { timeoutMs: 30_000 });
    if (Array.isArray(data)) return data;
    for (const key of ["profiles", "data", "value", "items"]) {
      if (Array.isArray(data[key])) return data[key];
    }
    return [];
  }

  async startProfile(profileId) {
    return this.request("GET", "/api/v2/profile/start", {
      params: { profileId },
      timeoutMs: this.timeoutMs,
    });
  }

  async stopProfile(profileId) {
    return this.request("GET", "/api/v2/profile/stop", {
      params: { profileId },
      timeoutMs: 30_000,
    });
  }

  async ping() {
    try {
      await this.listProfiles();
      return true;
    } catch {
      return false;
    }
  }
}
