# API Multilogin X — Hướng dẫn nhanh (VI)

API chạy **localhost** khi app Multilogin X đang mở.

## Cấu hình

| Mục | Giá trị |
|-----|---------|
| URL | `http://127.0.0.1:35000` |
| Auth | `Authorization: Bearer <token>` |
| Token | Settings → Automation |

## 3 lệnh quan trọng

```bash
# Danh sách profile
GET /api/v2/profile

# Mở profile
GET /api/v2/profile/start?profileId=UUID

# Đóng profile
GET /api/v2/profile/stop?profileId=UUID
```

## Python (khuyên dùng)

```python
from multilogin_client import MultiloginClient

with MultiloginClient() as c:
    for p in c.list_profiles_normalized():
        print(p.name, p.id)
    with c.profile("uuid") as s:
        print(s.cdp_url)
```

Repo đầy đủ: [Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)

## Tài liệu chính thức

- [Postman API](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
- [API beginners (EN)](https://multilogin.com/help/en_US/multilogin-x-api-beginners-guide)

## Mã giảm giá

| Mã | Dùng cho |
|----|----------|
| `SAAS50` | Gói browser mới |
| `MIN50` | Cloud Phone |

[Đăng ký / pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
