# Multilogin API Examples — Tiếng Việt

Repo open-source cộng đồng bởi [**@Anti-detect**](https://github.com/Anti-detect):  
**[github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)**

Ví dụ Python / Node / curl cho **Multilogin X Local API** — antidetect browser, quản lý đa tài khoản, tự động hóa Playwright & Selenium.

> Repo **không** thuộc Multilogin chính thức. Một số link pricing là partner referral (không tăng giá cho bạn).

---

## Mã giảm giá & link

| | |
|---|---|
| **Đăng ký / pricing** | [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) |
| **`SAAS50`** | Giảm 50% gói mới |
| **`MIN50`** | Giảm 50% Cloud Phone |

---

## Multilogin là gì?

- Mỗi **profile** = 1 trình duyệt riêng (fingerprint, cookie, storage)
- Nền tảng không link được các tài khoản của bạn
- **Local API** trên máy (`127.0.0.1:35000`) để script start/stop profile
- **Cloud Phone** cho app mobile-only

Dùng cho: Amazon/eBay, Facebook/Google Ads, affiliate, MMO, scraping hợp pháp.

---

## Bắt đầu trong 5 phút

```powershell
git clone https://github.com/Anti-detect/multilogin-api-examples.git
cd multilogin-api-examples\examples\python
pip install -r requirements.txt
$env:MULTILOGIN_TOKEN="token"
$env:MULTILOGIN_PROFILE_ID="uuid"
python health_check.py
```

Chi tiết: **[getting-started.md](getting-started.md)**

---

## Tài liệu tiếng Việt

| File | Nội dung |
|------|----------|
| [getting-started.md](getting-started.md) | Cài đặt từ đầu |
| [api-quickstart.md](api-quickstart.md) | API nhanh |
| [comparison.md](comparison.md) | So sánh antidetect |
| [../cloud-phone.md](../cloud-phone.md) | Cloud Phone + MIN50 |
| [../troubleshooting.md](../troubleshooting.md) | Sửa lỗi |

Tài liệu đầy đủ (EN): [docs/index.md](../index.md)

### Ngôn ngữ khác

| Ngôn ngữ | Link |
|----------|------|
| English | [../index.md](../index.md) |
| 中文 | [../zh/README.md](../zh/README.md) |
| Русский | [../ru/README.md](../ru/README.md) |
| Português | [../pt/README.md](../pt/README.md) |

---

## Code mẫu

```python
from multilogin_client import MultiloginClient

with MultiloginClient() as client:
    with client.profile("profile-uuid") as session:
        print(session.cdp_url)  # Playwright
```

| Script | Việc làm |
|--------|----------|
| `health_check.py` | Kiểm tra agent + token |
| `list_profiles.py` | Liệt kê profile |
| `batch_workflow.py` | Nhiều profile |
| `playwright_connect.py` | Tự động web |

---

## Lưu ý pháp lý & bảo mật

- Repo **không** thuộc Multilogin chính thức
- Không commit token lên GitHub
- Tuân thủ điều khoản nền tảng bạn thao tác

---

## Hỗ trợ

- Lỗi script trong repo: [GitHub Issues](https://github.com/Anti-detect/multilogin-api-examples/issues)
- Sản phẩm Multilogin: [Help Center](https://multilogin.com/help/)

---

**Mua / gia hạn:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
