from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
@app.get('/api/data')
def get_data():
    return {"msg": "API para frontend SPA"}
# Para rodar: uvicorn web.frontend_fastapi:app --reload
