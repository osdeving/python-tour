# Segurança FastAPI
from fastapi import FastAPI, Request
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import bcrypt
app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)
@app.post('/hash')
def hash_senha():
    senha = b'segredo'
    hash = bcrypt.hashpw(senha, bcrypt.gensalt())
    return {"hash": hash.decode()}
# Para rodar: uvicorn web.seguranca_fastapi:app --reload
