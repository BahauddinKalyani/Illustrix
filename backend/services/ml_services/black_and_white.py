import cv2

from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure

def black_and_white_fun(file_name: str, system_file_path: str) -> str:
    image = cv2.imread(system_file_path, cv2.IMREAD_GRAYSCALE)
    black_and_white_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.BLACKA_AND_WHITE_PATH + system_file_path.split("/")[-1]
    save_to_sub_folder(black_and_white_path, image)
    save_to_final_folder(system_file_path, image)
    return system_file_path