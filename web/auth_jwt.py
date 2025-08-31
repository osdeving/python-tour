from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET = "segredo"
# JWT
@app.get('/me')
def read_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return {"user": payload.get("sub")}
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido")
# Para rodar: pip install fastapi uvicorn python-jose
# Para autenticação completa, veja docs FastAPI
