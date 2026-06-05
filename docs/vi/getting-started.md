# Bắt đầu với Multilogin (Tiếng Việt)

Hướng dẫn từ zero → chạy API script đầu tiên.  
Repo: [@Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)

---

## Bước 1 — Tài khoản

1. Mở [bảng giá Multilogin](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
2. Nhập mã **`SAAS50`** (gói mới, giảm 50% nếu áp dụng được)
3. Tải **Multilogin X** cho Windows / macOS / Linux
4. Đăng nhập workspace

---

## Bước 2 — Tạo profile trình duyệt

1. **Create profile** trong app
2. Chọn **Mimic** (Chrome) hoặc **Stealthfox** (Firefox)
3. Fingerprint: Random hoặc chỉnh OS, màn hình, timezone, ngôn ngữ
4. Gán **proxy** (residential có sẵn trên gói trả phí, hoặc proxy riêng)
5. Copy **Profile UUID** — dùng cho `MULTILOGIN_PROFILE_ID`

---

## Bước 3 — Bật API

1. **Settings → Automation**
2. **Generate automation token** → lưu vào biến môi trường
3. Giữ app chạy nền — API lắng nghe `http://127.0.0.1:35000`

---

## Bước 4 — Chạy script từ repo

```powershell
git clone https://github.com/Anti-detect/multilogin-api-examples.git
cd multilogin-api-examples\examples\python
pip install -r requirements.txt

$env:MULTILOGIN_TOKEN="dán-token-vào-đây"
$env:MULTILOGIN_PROFILE_ID="dán-uuid-profile"
python health_check.py
python list_profiles.py
python start_profile.py
```

Nếu `health_check` báo **OK** → setup thành công.

---

## Bước 5 — Tự động hóa nâng cao

```python
from multilogin_client import MultiloginClient

with MultiloginClient() as client:
    with client.profile("uuid-của-bạn") as session:
        print(session.cdp_url)   # gắn Playwright
```

| Script | Mục đích |
|--------|----------|
| `playwright_connect.py` | Điều khiển web bằng Playwright |
| `selenium_connect.py` | Selenium |
| `batch_workflow.py` | Nhiều profile |
| `session_context_demo.py` | Tự động stop khi lỗi |

Chi tiết: [api-quickstart.md](api-quickstart.md) · [browser-automation.md](../browser-automation.md)

---

## Cloud Phone (app mobile)

Dùng khi nền tảng **chỉ có app** (một số social, fintech).  
Mã **`MIN50`** — giảm 50% Cloud Phone.  
Xem [cloud-phone.md](../cloud-phone.md).

---

## Lỗi thường gặp

| Lỗi | Cách sửa |
|-----|----------|
| Connection refused | Mở app Multilogin X |
| 401 Unauthorized | Tạo lại automation token |
| Timeout khi start | Tăng timeout, thử proxy khác |
| Playwright không kết nối | Set `MULTILOGIN_CDP_URL` từ output start |

Đầy đủ: [troubleshooting.md](../troubleshooting.md)

---

**Gia hạn / mua:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
