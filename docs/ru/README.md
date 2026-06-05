# Примеры Multilogin API — антидетект-браузер и автоматизация

Открытый репозиторий сообщества от [**@Anti-detect**](https://github.com/Anti-detect):  
**[github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)**

Примеры на Python / Node.js / curl для **Multilogin X Local API** — антидетект-профили, изоляция отпечатков, управление несколькими аккаунтами, автоматизация через Playwright и Selenium.

> Отказ от ответственности: проект не связан с Multilogin Ltd. Некоторые ссылки на pricing — партнёрские (цена для вас не меняется).

---

## Промокоды и ссылки

| | |
|---|---|
| **Регистрация / pricing** | [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) |
| **`SAAS50`** | −50% на новые подписки браузера |
| **`MIN50`** | −50% на Cloud Phone |

---

## Что такое Multilogin?

- Каждый **профиль** = отдельный браузер (отпечаток, cookies, storage)
- Платформы не могут связать ваши аккаунты между собой
- **Local API** на localhost (`127.0.0.1:35000`) для start/stop профилей из скриптов
- **Cloud Phone** для мобильных приложений без десктопной версии

Применение: маркетплейсы, таргетированная реклама, партнёрский маркетинг, автоматизация, легальный сбор данных.

---

## Быстрый старт за 5 минут

```bash
git clone https://github.com/Anti-detect/multilogin-api-examples.git
cd multilogin-api-examples/examples/python
pip install -r requirements.txt
export MULTILOGIN_TOKEN="your-token"
export MULTILOGIN_PROFILE_ID="profile-uuid"
python health_check.py
```

Подробнее: **[getting-started.md](getting-started.md)**

---

## Пример кода

```python
from multilogin_client import MultiloginClient

with MultiloginClient() as client:
    with client.profile("profile-uuid") as session:
        print(session.cdp_url)  # Playwright CDP
```

| Скрипт | Назначение |
|--------|------------|
| `health_check.py` | Проверка agent + token |
| `list_profiles.py` | Список профилей |
| `batch_workflow.py` | Пакетный start/stop |
| `playwright_connect.py` | Web-автоматизация |

Полная документация (EN): [docs/index.md](../index.md)

---

## Другие языки

| Язык | Ссылка |
|------|--------|
| English | [../index.md](../index.md) |
| 中文 | [../zh/README.md](../zh/README.md) |
| Tiếng Việt | [../vi/README.md](../vi/README.md) |
| Português | [../pt/README.md](../pt/README.md) |

---

## Поддержка

- Ошибки в репозитории: [GitHub Issues](https://github.com/Anti-detect/multilogin-api-examples/issues)
- Поддержка Multilogin: [Help Center](https://multilogin.com/help/)

---

**Купить / продлить:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
