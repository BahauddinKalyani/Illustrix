# import cv2
# TODO: Change to Opencv
import cv2 
import numpy as np

from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure, ml_constants

def painting_fun(file_name: str, system_file_path: str, factor: int) -> str:
    image = cv2.imread(system_file_path)
    image_clear = cv2.medianBlur(image, factor)
    image_clear = cv2.medianBlur(image_clear, factor)
    image_clear = cv2.medianBlur(image_clear, factor)
    image_clear = cv2.edgePreservingFilter(image_clear, sigma_s=10)
    image_filter = cv2.bilateralFilter(image_clear, 3, 10, 5)
    for _ in range(2):
        image_filter = cv2.bilateralFilter(image_clear, 3, 20, 10)
    for _ in range(3):
        image_filter = cv2.bilateralFilter(image_clear, 5, 30, 10)
    for _ in range(3):
        image_filter = cv2.bilateralFilter(image_clear, 5, 40, 10)
    gaussian_mask = cv2.GaussianBlur(image_filter, (9,9), 3)
    painted_image = cv2.addWeighted(image_filter, 1.5, gaussian_mask, -0.5, 0)
    painted_image = cv2.addWeighted(painted_image, ml_constants.SHAPRNESS_FACTOR, gaussian_mask, -(ml_constants.SHAPRNESS_FACTOR-1), 10)
    painting_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.PAINTING_PATH + system_file_path.split("/")[-1]
    # image = cv2.imread(system_file_path)
    # image_clear = cv2.edgePreservingFilter(image, sigma_s=5)
    # image_filter = cv2.bilateralFilter(image_clear, 3, 10, 5)
    # gaussian_mask = cv2.GaussianBlur(image_filter, (5,5), 5)
    # painted_image = cv2.addWeighted(image_filter, 1.5, gaussian_mask, -0.5, 0)
    # painting_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.PAINTING_PATH + system_file_path.split("/")[-1]
    save_to_sub_folder(painting_path, painted_image)
    save_to_final_folder(system_file_path, painted_image)
    return system_file_path