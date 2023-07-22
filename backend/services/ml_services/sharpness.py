# import cv2
# TODO: Change to Opencv
from PIL import Image, ImageEnhance
import numpy as np

from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure

def sharpness_fun(file_name: str, system_file_path: str, factor: int) -> str:
    image = Image.open(system_file_path)
    enhancer = ImageEnhance.Sharpness(image)
    sharpness_image = enhancer.enhance(factor)
    sharpness_image = np.array(sharpness_image)
    sharpness_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.SHARPNESS_PATH + system_file_path.split("/")[-1]
    save_to_sub_folder(sharpness_path, sharpness_image)
    save_to_final_folder(system_file_path, sharpness_image)
    return system_file_path