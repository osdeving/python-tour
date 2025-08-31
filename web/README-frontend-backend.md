# 9. Frontend + Backend

Este módulo cobre:
- Servindo HTML (templates Jinja2, Django Templates)
- APIs para frontend SPA (React, Vue, Angular)
- CORS (Cross-Origin Resource Sharing)
- Integração com Next.js, Nuxt ou similares

## Exemplos
- `frontend_flask.py`: serve HTML com Flask
- `frontend_fastapi.py`: API com CORS para SPA
- `frontend_django.py`: referência a templates Django

## Como rodar
1. Instale dependências:
   ```bash
   pip install flask fastapi uvicorn django
   ```
2. Execute Flask:
   ```bash
   python web/frontend_flask.py
   ```
3. Execute FastAPI:
   ```bash
   uvicorn web.frontend_fastapi:app --reload
   ```
4. Para Django, crie templates e rode:
   ```bash
   python manage.py runserver
   ```

## Explicação
- Templates servem HTML dinâmico.
- APIs com CORS permitem integração com SPAs.
- Integração com frameworks modernos é feita via APIs REST.

Referências:
- [Jinja2](https://jinja.palletsprojects.com/)
- [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
