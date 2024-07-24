from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_uri: str
    database_name: str
    predibase_api_key: str
    username: str = "admin"
    password: str = "admin"

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()


async def get_db():
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongodb_uri)
    db = client[settings.database_name]
    return db
