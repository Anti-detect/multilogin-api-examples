# Multilogin 快速入门（中文）

从零到第一次 API 调用 — 然后阅读 [api-quickstart.md](../api-quickstart.md) 和 [examples/python](../../examples/python/)。

> 示例仓库：[github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)

---

## 1. 注册与安装

| 步骤 | 操作 |
|------|------|
| 注册 | 打开 [定价页面](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)，结账时使用 **`SAAS50`** |
| 下载 | [multilogin.com](https://multilogin.com/) → 下载 Multilogin X |
| 登录 | 使用工作区邮箱登录 |

---

## 2. 创建浏览器配置文件

1. 工作区 → **Create profile**
2. 浏览器：**Mimic** (Chromium) 或 **Stealthfox** (Firefox)
3. 指纹：随机或手动设置（OS、屏幕、时区、语言）
4. 代理：内置住宅代理（付费计划）或自定义 SOCKS5/HTTP

从配置文件设置中复制 **profile UUID** — 用于 `MULTILOGIN_PROFILE_ID`。

---

## 3. 启用 API

1. **Settings → Automation → Generate** 生成 automation token
2. 确保 Multilogin X 桌面客户端正在运行
3. Local API 默认地址：`http://127.0.0.1:35000`

---

## 4. 运行健康检查

```bash
git clone https://github.com/Anti-detect/multilogin-api-examples.git
cd multilogin-api-examples/examples/python
pip install -r requirements.txt
cp .env.example .env   # 填入 token 和 profile id
python health_check.py
```

成功输出应包含 agent 状态和 profile 数量。

---

## 5. 启动配置文件

```bash
python start_profile.py
```

或使用 context manager 自动停止：

```bash
python session_context_demo.py
```

---

## Cloud Phone

移动应用专用工作流 — 结账时使用 **`MIN50`** 享受 50% 折扣。

详见 [cloud-phone.md](../cloud-phone.md)

---

## 下一步

| 文档 | 内容 |
|------|------|
| [api-quickstart.md](../api-quickstart.md) | API 认证与端点 |
| [browser-automation.md](../browser-automation.md) | Playwright / Selenium |
| [troubleshooting.md](../troubleshooting.md) | 常见错误修复 |

---

**购买 / 续费：** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
