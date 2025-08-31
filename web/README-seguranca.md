# 11. Segurança em Aplicações Web

Este módulo cobre:
- CSRF, XSS, SQL Injection
- Rate limiting
- Hash de senhas (bcrypt, argon2)
- Helmet para headers HTTP

## Exemplos
- `seguranca_flask.py`: XSS e hash de senha
- `seguranca_fastapi.py`: hash de senha e HTTPS
- `seguranca_django.py`: referência a segurança Django

## Como rodar
1. Instale dependências:
   ```bash
   pip install flask fastapi uvicorn bcrypt django
   ```
2. Execute Flask:
   ```bash
   python web/seguranca_flask.py
   ```
3. Execute FastAPI:
   ```bash
   uvicorn web.seguranca_fastapi:app --reload
   ```
4. Para Django, veja settings.py

## Explicação
- Sempre sanitize entradas para evitar XSS/SQL Injection.
- Use hash seguro para senhas.
- Middlewares ajudam a proteger headers e limitar requisições.

Referência:
- [OWASP Top 10](https://owasp.org/Top10/)
