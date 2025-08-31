from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
@app.get('/items/{item_id}')
def get_item(item_id: int = Path(...), q: str = Query(None)):
    return {"item_id": item_id, "q": q}
@app.post('/items/')
def create_item(item: Item):
    return item
# Para rodar: uvicorn web.api_rest:app --reload
