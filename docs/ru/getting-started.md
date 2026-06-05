# Быстрый старт с Multilogin (RU)

От нуля до первого API-вызова — затем [api-quickstart.md](../api-quickstart.md) и [examples/python](../../examples/python/).

> Репозиторий: [github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)

---

## 1. Регистрация и установка

| Шаг | Действие |
|-----|----------|
| Регистрация | [Страница pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — промокод **`SAAS50`** |
| Скачать | [multilogin.com](https://multilogin.com/) → Multilogin X для вашей ОС |
| Вход | Email рабочей области |

---

## 2. Создание профиля браузера

1. Workspace → **Create profile**
2. Браузер: **Mimic** (Chromium) или **Stealthfox** (Firefox)
3. Отпечаток: случайный или вручную (OS, экран, timezone, язык)
4. Прокси: встроенный residential (платные планы) или свой SOCKS5/HTTP

Скопируйте **profile UUID** из настроек — нужен для `MULTILOGIN_PROFILE_ID`.

---

## 3. Включение API

1. **Settings → Automation → Generate** — automation token
2. Multilogin X должен быть запущен и авторизован
3. Local API по умолчанию: `http://127.0.0.1:35000`

---

## 4. Health check

```bash
git clone https://github.com/Anti-detect/multilogin-api-examples.git
cd multilogin-api-examples/examples/python
pip install -r requirements.txt
cp .env.example .env
python health_check.py
```

---

## 5. Запуск профиля

```bash
python start_profile.py
python session_context_demo.py   # auto-stop через context manager
```

---

## Cloud Phone

Для mobile-only приложений — промокод **`MIN50`** (−50%).

Подробнее: [cloud-phone.md](../cloud-phone.md)

---

## Дальше

| Документ | Содержание |
|----------|------------|
| [api-quickstart.md](../api-quickstart.md) | Auth и endpoints |
| [browser-automation.md](../browser-automation.md) | Playwright / Selenium |
| [troubleshooting.md](../troubleshooting.md) | Исправление ошибок |

---

**Купить / продлить:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
