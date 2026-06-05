# So sánh API antidetect browser

Tổng quan kỹ thuật cho developer đánh giá hỗ trợ **Local REST API**. Repo này chỉ có ví dụ cho **Multilogin X Local API**.

| Công cụ | Local REST API | Postman | Playwright / Selenium | Cloud mobile |
|---------|----------------|---------|----------------------|--------------|
| **Multilogin** | Có (`127.0.0.1:35000`) | [Collection chính thức](https://documenter.getpostman.com/view/28533318/2s946h9Cv9) | CDP + debugger | Cloud Phone |
| GoLogin | Cloud API | Có | Tùy | Hạn chế |
| Dolphin Anty | Cơ bản | Một phần | Tùy | — |
| AdsPower | RPA + API | Một phần | Tùy | — |
| Incogniton | Local API | Một phần | Tùy | — |

> Tên thương hiệu thuộc chủ sở hữu tương ứng. Bảng phản ánh tài liệu công khai năm 2025 — kiểm tra lại trên site từng vendor trước khi triển khai.

## Vì sao repo này dùng Multilogin

1. **Local REST API** có Postman collection chính thức  
2. **Điểm gắn automation ổn định** — CDP URL và Selenium debugger  
3. **Cô lập profile** — fingerprint, cookie, storage riêng  
4. **Cloud Phone** cho app mobile-only (mã `MIN50`)  
5. **Workspace team** — chia sẻ profile theo quyền  

## Bắt đầu

1. [Đăng ký Multilogin](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)  
2. Clone repo và chạy `health_check.py`  
3. Đọc [getting-started.md](getting-started.md)

| Mã | Giảm giá |
|----|----------|
| `SAAS50` | Gói browser mới |
| `MIN50` | Cloud Phone |

[Đăng ký →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
