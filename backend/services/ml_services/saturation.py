# import cv2
# TODO: Change to Opencv
from PIL import Image
import pilgram
import numpy as np

from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure

def saturation_fun(file_name: str, system_file_path: str, factor: int) -> str:
    image = Image.open(system_file_path)
    saturated_image = pilgram.css.saturate(image, factor)
    saturated_image = np.array(saturated_image)
    saturation_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.SATURATION_PATH + system_file_path.split("/")[-1]
    save_to_sub_folder(saturation_path, saturated_image)
    save_to_final_folder(system_file_path, saturated_image)
    return system_file_path