# import cv2
# TODO: Change to Opencv
from PIL import Image, ImageEnhance
import numpy as np

from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure

def contrast_fun(file_name: str, system_file_path: str, factor: int) -> str:
    image = Image.open(system_file_path)
    enhancer = ImageEnhance.Contrast(image)
    contrasted_image = enhancer.enhance(factor)
    contrasted_image = np.array(contrasted_image)
    contrast_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.CONTRAST_PATH + system_file_path.split("/")[-1]
    save_to_sub_folder(contrast_path, contrasted_image)
    save_to_final_folder(system_file_path, contrasted_image)
    return system_file_path