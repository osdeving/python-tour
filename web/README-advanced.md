# Exemplos avançados de web com Python

Este diretório contém exemplos usando Flask e FastAPI.

## FastAPI
- `fastapi_app.py`: Exemplo básico de FastAPI.
  - Para rodar:
    ```bash
    pip install fastapi uvicorn
    uvicorn web.fastapi_app:app --reload
    ```
  - Acesse `http://localhost:8000`.

## API com Flask
- `api_flask.py`: Exemplo de rota API REST usando Flask.
  - Para rodar:
    ```bash
    pip install flask
    python web/app.py
    ```
  - Acesse `http://localhost:5000/api/ping`.

## Modularização
- Use Blueprints (Flask) ou APIRouter (FastAPI) para organizar rotas.

Consulte cada arquivo para exemplos práticos e adapte conforme seu projeto.
