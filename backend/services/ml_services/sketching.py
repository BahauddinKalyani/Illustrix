import cv2

from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure

def dodgeV2(x, y):
    return cv2.divide(x, 255-y, scale=250)

def sketching_fun(file_name: str, system_file_path: str, factor: int) -> str:
    image = cv2.imread(system_file_path)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21,21), sigmaX=0, sigmaY=0)
    sketched_img = dodgeV2(img_gray, img_smoothing)
    sketching_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.SKETCHING_PATH + system_file_path.split("/")[-1]
    save_to_sub_folder(sketching_path, sketched_img)
    save_to_final_folder(system_file_path, sketched_img)
    return system_file_path