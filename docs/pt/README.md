# Exemplos Multilogin API — navegador antidetect e automação

Repositório open-source da comunidade [**@Anti-detect**](https://github.com/Anti-detect):  
**[github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)**

Exemplos em Python / Node.js / curl para a **Multilogin X Local API** — perfis antidetect, isolamento de fingerprint, multi-contas, automação com Playwright e Selenium.

> Aviso: projeto independente, não afiliado à Multilogin Ltd. Alguns links de pricing são de parceiro (sem custo extra para você).

---

## Códigos promocionais

| | |
|---|---|
| **Cadastro / pricing** | [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) |
| **`SAAS50`** | 50% off em novas assinaturas de browser |
| **`MIN50`** | 50% off em Cloud Phone |

---

## O que é Multilogin?

- Cada **profile** = navegador isolado (fingerprint, cookies, storage)
- Plataformas não conseguem vincular suas contas
- **Local API** em `127.0.0.1:35000` para start/stop via script
- **Cloud Phone** para apps mobile-only

Uso comum: e-commerce (Amazon/Mercado Livre), anúncios Facebook/Google, marketing de afiliados, automação, scraping legal.

---

## Início rápido (5 min)

```bash
git clone https://github.com/Anti-detect/multilogin-api-examples.git
cd multilogin-api-examples/examples/python
pip install -r requirements.txt
export MULTILOGIN_TOKEN="seu-token"
export MULTILOGIN_PROFILE_ID="uuid-do-profile"
python health_check.py
```

Detalhes: **[getting-started.md](getting-started.md)**

---

## Exemplo de código

```python
from multilogin_client import MultiloginClient

with MultiloginClient() as client:
    with client.profile("profile-uuid") as session:
        print(session.cdp_url)  # Playwright CDP
```

Documentação completa (EN): [docs/index.md](../index.md)

---

## Outros idiomas

| Idioma | Link |
|--------|------|
| English | [../index.md](../index.md) |
| 中文 | [../zh/README.md](../zh/README.md) |
| Русский | [../ru/README.md](../ru/README.md) |
| Tiếng Việt | [../vi/README.md](../vi/README.md) |

---

## Suporte

- Bugs neste repo: [GitHub Issues](https://github.com/Anti-detect/multilogin-api-examples/issues)
- Produto Multilogin: [Help Center](https://multilogin.com/help/)

---

**Comprar / renovar:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
