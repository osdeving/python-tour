from fastapi import FastAPI, File, UploadFile, Query
from typing import List
app = FastAPI()

@app.get('/items/')
def list_items(page: int = Query(1), size: int = Query(10), q: str = Query(None)):
    # Paginação, filtro, ordenação
    return {"page": page, "size": size, "q": q}

@app.post('/upload/')
def upload_file(file: UploadFile = File(...)):
    content = file.file.read()
    return {"filename": file.filename, "size": len(content)}

# Documentação automática: acesse /docs ou /redoc
# Para rodar: uvicorn web.api_avancada:app --reload
