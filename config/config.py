from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Agents"
    url_db: str
    name_db: str
    api_version: str


settings = Settings()