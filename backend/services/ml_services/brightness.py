# import cv2
# TODO: Change to Opencv
from PIL import Image, ImageEnhance
import numpy as np

from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure

def brightness_fun(file_name: str, system_file_path: str, factor: int) -> str:
    image = Image.open(system_file_path)
    enhancer = ImageEnhance.Brightness(image)
    brightness_image = enhancer.enhance(factor)
    brightness_image = np.array(brightness_image)
    brightness_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.BRIGHTNESS_PATH + system_file_path.split("/")[-1]
    save_to_sub_folder(brightness_path, brightness_image)
    save_to_final_folder(system_file_path, brightness_image)
    return system_file_path