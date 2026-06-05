# Primeiros passos com Multilogin (PT-BR)

Do zero à primeira chamada de API — depois veja [api-quickstart.md](../api-quickstart.md) e [examples/python](../../examples/python/).

> Repositório: [github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)

---

## 1. Conta e instalação

| Passo | Ação |
|-------|------|
| Cadastro | [Página de pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — código **`SAAS50`** |
| Download | [multilogin.com](https://multilogin.com/) → Multilogin X |
| Login | Email do workspace |

---

## 2. Criar um profile de browser

1. Workspace → **Create profile**
2. Browser: **Mimic** (Chromium) ou **Stealthfox** (Firefox)
3. Fingerprint: aleatório ou manual (OS, tela, fuso, idioma)
4. Proxy: residential integrado (planos pagos) ou SOCKS5/HTTP próprio

Copie o **profile UUID** das configurações — use em `MULTILOGIN_PROFILE_ID`.

---

## 3. Habilitar API

1. **Settings → Automation → Generate** — automation token
2. Multilogin X aberto e logado
3. Local API padrão: `http://127.0.0.1:35000`

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

## 5. Iniciar profile

```bash
python start_profile.py
python session_context_demo.py
```

---

## Cloud Phone

Apps somente mobile — código **`MIN50`** (50% off).

Veja [cloud-phone.md](../cloud-phone.md)

---

## Próximos passos

| Doc | Conteúdo |
|-----|----------|
| [api-quickstart.md](../api-quickstart.md) | Auth e endpoints |
| [browser-automation.md](../browser-automation.md) | Playwright / Selenium |
| [troubleshooting.md](../troubleshooting.md) | Correção de erros |

---

**Comprar / renovar:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
