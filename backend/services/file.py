import os
from config.settings import file_structure
import cv2
import numpy as np

def create_base_structure(email: str) -> None:
    base_folder = file_structure.USER_DATA + email
    
    is_exist = os.path.exists(base_folder)
    if is_exist == False:
        os.mkdir(base_folder)
        for i in file_structure.BASE_STRUCTURE:
            sub_folders_path = base_folder + i
            os.mkdir(sub_folders_path)

def get_file_path_from_url(body: dict) -> str:
    global_url = body["image_url"]
    file_name = body["image_url"].split("/")[-1]
    system_path_index = body["image_url"].find("/static")
    system_path = "." + body["image_url"][system_path_index:]
    background_image = ""
    if "background_url" in body:
        background_image_index = body["background_url"].find("/static")
        background_image = "." + body["background_url"][background_image_index:]
    return file_name, system_path, global_url, background_image

def save_to_final_folder(path: str, image: np.ndarray) -> None:
    cv2.imwrite(path, image)

def save_to_sub_folder(path: str, image: np.ndarray) -> None:
    cv2.imwrite(path, image)