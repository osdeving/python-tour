# 3. Frameworks Web em Python

Este módulo cobre:
- Flask (minimalista)
- FastAPI (async, OpenAPI)
- Django (completo, MVC, ORM)
- Comparação entre frameworks

## Exemplos
- `flask_exemplo.py`: app Flask simples
- `fastapi_exemplo.py`: app FastAPI simples
- `django_exemplo.py`: comandos Django

## Como rodar
1. Instale dependências:
   ```bash
   pip install flask fastapi uvicorn django
   ```
2. Execute Flask:
   ```bash
   python web/flask_exemplo.py
   ```
3. Execute FastAPI:
   ```bash
   uvicorn web.fastapi_exemplo:app --reload
   ```
4. Para Django, crie projeto:
   ```bash
   django-admin startproject exemplo_django
   ```

## Explicação
- Flask: ideal para projetos pequenos e APIs simples.
- FastAPI: APIs rápidas, validação automática, async.
- Django: completo, MVC, ORM, ideal para sistemas grandes.

Referências:
- [Flask](https://flask.palletsprojects.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Django](https://www.djangoproject.com/)
