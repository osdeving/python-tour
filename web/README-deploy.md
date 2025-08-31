# 12. Deploy e Produção

Este módulo cobre:
- WSGI vs ASGI
- Gunicorn, Uvicorn, Daphne
- Docker para empacotar apps
- CI/CD (GitHub Actions, GitLab CI, etc.)
- Deploy em serviços (Heroku, Railway, Vercel, AWS, GCP, Azure)

## Exemplos
- `deploy_flask.py`: comandos e Dockerfile para Flask
- `deploy_fastapi.py`: comandos e Dockerfile para FastAPI
- `deploy_django.py`: comandos e Dockerfile para Django

## Como rodar
1. Instale dependências:
   ```bash
   pip install gunicorn uvicorn daphne flask fastapi django
   ```
2. Execute comandos de deploy conforme exemplos.
3. Use Docker para empacotar e rodar apps.

## Explicação
- WSGI é padrão para apps síncronos (Flask, Django).
- ASGI é padrão para apps assíncronos (FastAPI, Django Channels).
- Docker facilita deploy em qualquer ambiente.
- CI/CD automatiza testes e deploy.

Referências:
- [Gunicorn](https://gunicorn.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Daphne](https://github.com/django/daphne)
- [Docker](https://docs.docker.com/)
