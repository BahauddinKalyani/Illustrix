import cv2

from services.ml_services.background_remove import background_remove_fun
from services.ml_services.background_blur import background_blur_fun
from services.ml_services.merge_two_images import merge_two_images_fun
from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure, ml_constants

def background_remove_and_blur_fun(file_name: str, system_file_path: str, background_path: str) -> str:
    bg_remove = background_remove_fun(file_name = file_name, system_file_path = system_file_path)
    foreground = cv2.imread(bg_remove, cv2.IMREAD_COLOR)
    bg_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.USER_BLURRED_BACKGROUND_PATH + background_path.split("/")[-1]
    background = cv2.imread(background_path)
    background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))
    blurred_background = cv2.GaussianBlur(background, (ml_constants.BLUR_FACTOR, ml_constants.BLUR_FACTOR), 0)
    save_to_sub_folder(bg_path, blurred_background)
    combined_image_path = merge_two_images_fun(foregrond_image_path = bg_remove, background_image_path = bg_path, system_file_path = system_file_path)
    combined_image = cv2.imread(combined_image_path)
    save_to_final_folder(system_file_path, combined_image)
    return system_file_path