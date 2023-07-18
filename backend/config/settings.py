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

class Constants(BaseSettings):
    SUCCESS_SIGNUP: str = "Successfully Singed Up!"
    SUCCESS_LOGIN: str = "Successfully Logged In!"
    INVALID_LOGIN: str = "Invalid Login!"
    ERROR: str = "Error Occured. Please Try again leter!"
    SUCCESSFULLY_PERFORMED: str = "Successfully Performed!"

constants = Constants()

class FileStructure(BaseSettings):
    BASE_STRUCTURE: list = ["/upload", "/final", "/background_remove", "/background", "/background_blur", "/combined_image"]
    USER_DATA: str = "./static/user_data/"
    STATIC_FOLDER: str = "./static/"
    MODEL_FOLDER: str = "./services/ml_services/models/"
    FINAL_IMAGE_PATH: str = "/final"
    BACKGROUND_REMOVE_PATH: str = "/background_remove/"
    USER_BACKGROUND_PATH: str = "/background/"
    USER_BLURRED_BACKGROUND_PATH: str = "/background_blur/"
    UPLOAD_IMAGE_PATH: str = "/upload"
    USER_COMBINED_IMAGE_PATH: str = "/combined_image/"

file_structure = FileStructure()

class MLConstants(BaseSettings):
    BLUR_FACTOR: int = 25

ml_constants = MLConstants()