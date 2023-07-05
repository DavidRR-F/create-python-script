from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    your_secret: str

    class Config:
        env_file = ".env.example"

settings = Settings()