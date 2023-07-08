from pydantic import BaseSettings

class DBSettings(BaseSettings):
    db_name: str = "illustrix"
    db_host: str = "localhost"
    db_port: int = 27017

db_settings = DBSettings()

class JWT(BaseSettings):
    JWT_Secret: str = "Femj4ul1V2Xk3A3Amy6w7cE9gVAdn96Y"
    JWT_Expiry_Time: int = 86400
    FMT: str = "%Y-%m-%d %H:%M:%S.%f"

jwt_setting = JWT()