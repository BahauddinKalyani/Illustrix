from pydantic import BaseSettings

class DBSettings(BaseSettings):
    db_name: str = "illustrix"
    db_host: str = "localhost"
    db_port: int = 27017

db_settings = DBSettings()
