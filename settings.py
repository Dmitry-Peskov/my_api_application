__all__ = ["db_config"]

from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings

DOT_ENV_FILE_DIRECTORY = Path(__file__).absolute().parent / ".env"
load_dotenv(DOT_ENV_FILE_DIRECTORY)


class DatabaseSettings(BaseSettings):
    host: str
    port: int
    name: str
    login: str
    password: str

    class Config:
        env_prefix = "DB_"

    @property
    def dsn(self) -> str:
        return f"postgresql+asyncpg://{self.login}:{self.password}@{self.host}:{self.port}/{self.name}"


db_config = DatabaseSettings()
