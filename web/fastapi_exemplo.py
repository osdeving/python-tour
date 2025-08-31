from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"mensagem": "FastAPI rápido e moderno!"}
# Para rodar: uvicorn web.fastapi_exemplo:app --reload
