from pydantic import BaseSettings

class Settings(BaseSettings):
    your_secret: str

    class Config:
        env_file = ".env"

settings = Settings()