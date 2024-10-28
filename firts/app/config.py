from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRET_KEY: str  # Добавляем SECRET_KEY
    ALGORITHM: str # Добавляем ALGORITHM

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Указано использование .env файла
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

print(settings.DATABASE_URL)