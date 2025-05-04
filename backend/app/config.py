from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_username: str = "postgres"
    database_password: str
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_name: str

    secret_key: str #openssl rand -hex 32
    algorithm: str = "HS256"
    access_token_expires_minutes: int = 120

    class Config:
        env_file = "Zeyora.env"

environment = Settings()