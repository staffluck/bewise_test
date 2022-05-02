from pydantic import BaseSettings
from sqlalchemy.engine.url import URL


class Settings(BaseSettings):

    DB_DRIVER: str = "postgres"
    DB_HOST: str = "db"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password"
    DB_DATABASE: str = "postgres"

    @property
    def DB_DSN(self) -> URL:
        return URL.create(
            self.DB_DRIVER,
            self.DB_USER,
            self.DB_PASSWORD,
            self.DB_HOST,
            self.DB_PORT,
            self.DB_DATABASE,
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
