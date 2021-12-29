from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url_new: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"



settings = Settings()