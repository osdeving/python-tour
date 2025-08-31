# 8. Autenticação e Autorização

Este módulo cobre:
- Cookies e sessões
- JWT (JSON Web Tokens)
- OAuth2
- Autorização baseada em papéis (RBAC)

## Exemplos
- `auth_jwt.py`: exemplo JWT com FastAPI
- `auth_flask.py`: exemplo de sessão/cookie com Flask
- `auth_django.py`: referência à autenticação do Django

## Como rodar
1. Instale dependências:
   ```bash
   pip install fastapi uvicorn python-jose flask django
   ```
2. Execute Flask:
   ```bash
   python web/auth_flask.py
   ```
3. Execute FastAPI:
   ```bash
   uvicorn web.auth_jwt:app --reload
   ```
4. Para Django, crie superusuário:
   ```bash
   python manage.py createsuperuser
   ```

## Explicação
- Cookies/sessões guardam estado do usuário.
- JWT é usado para autenticação stateless.
- OAuth2 é padrão para login com terceiros.
- RBAC controla acesso por papéis.

Referências:
- [OAuth2 RFC](https://datatracker.ietf.org/doc/html/rfc6749)
- [FastAPI Auth](https://fastapi.tiangolo.com/tutorial/security/)
- [Django Auth](https://docs.djangoproject.com/en/4.0/topics/auth/)
