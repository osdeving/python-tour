from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Bem-vindo ao exemplo FastAPI!</h1>"

# Para rodar: uvicorn fastapi_app:app --reload
