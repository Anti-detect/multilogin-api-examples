# Multilogin API 示例 — 反检测浏览器自动化

社区开源项目，维护者 [**@Anti-detect**](https://github.com/Anti-detect)：  
**[github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)**

为 **Multilogin X Local API** 提供 Python / Node.js / curl 示例 — 反检测浏览器、指纹隔离、多账号管理、Playwright 与 Selenium 自动化。

> 免责声明：本项目与 Multilogin Ltd. 无官方关联。部分定价链接为合作伙伴推荐链接，不影响您的购买价格。

---

## 优惠码与链接

| | |
|---|---|
| **注册 / 定价** | [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) |
| **`SAAS50`** | 新浏览器订阅 50% 折扣 |
| **`MIN50`** | Cloud Phone 50% 折扣 |

---

## Multilogin 是什么？

- 每个 **配置文件 (profile)** = 独立浏览器环境（指纹、Cookie、存储隔离）
- 平台无法将您的多个账号关联在一起
- **Local API** 运行在本地 (`127.0.0.1:35000`)，用于脚本启动/停止配置文件
- **Cloud Phone** 适用于仅支持移动端的应用

常见用途：跨境电商 (Amazon/eBay)、Facebook/Google 广告、联盟营销、自动化测试、合规数据采集。

---

## 5 分钟快速开始

```bash
git clone https://github.com/Anti-detect/multilogin-api-examples.git
cd multilogin-api-examples/examples/python
pip install -r requirements.txt
export MULTILOGIN_TOKEN="your-token"
export MULTILOGIN_PROFILE_ID="profile-uuid"
python health_check.py
```

详细步骤：**[getting-started.md](getting-started.md)**

---

## 示例代码

```python
from multilogin_client import MultiloginClient

with MultiloginClient() as client:
    with client.profile("profile-uuid") as session:
        print(session.cdp_url)  # Playwright CDP
```

| 脚本 | 功能 |
|------|------|
| `health_check.py` | 检测 agent 与 token |
| `list_profiles.py` | 列出配置文件 |
| `batch_workflow.py` | 批量启动/停止 |
| `playwright_connect.py` | Playwright 自动化 |

完整英文文档：[docs/index.md](../index.md)

---

## 其他语言

| 语言 | 链接 |
|------|------|
| English | [../index.md](../index.md) |
| Tiếng Việt | [../vi/README.md](../vi/README.md) |
| Русский | [../ru/README.md](../ru/README.md) |
| Português | [../pt/README.md](../pt/README.md) |

---

## 支持与反馈

- 本仓库问题：[GitHub Issues](https://github.com/Anti-detect/multilogin-api-examples/issues)
- Multilogin 产品支持：[Help Center](https://multilogin.com/help/)

---

**购买 / 续费：** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
