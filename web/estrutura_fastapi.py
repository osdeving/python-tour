# Estrutura de projeto em FastAPI
# main.py
from fastapi import FastAPI
from routers import user_router
app = FastAPI()
app.include_router(user_router)
# routers/user_router.py
# from fastapi import APIRouter
# user_router = APIRouter()
# @user_router.get('/user/{username}')
# def get_user(username: str):
#     return {"username": username}
# Para rodar: uvicorn main:app --reload
