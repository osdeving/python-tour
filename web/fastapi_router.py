from fastapi import APIRouter

router = APIRouter()

@router.get("/hello-fastapi")
def hello():
    return {"message": "Hello from FastAPI Router!"}
