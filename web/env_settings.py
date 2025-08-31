# Uso de .env e pydantic-settings
# .env
# SECRET_KEY=segredo
# settings.py
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    secret_key: str
    class Config:
        env_file = ".env"
settings = Settings()
print(settings.secret_key)
# pip install pydantic-settings
