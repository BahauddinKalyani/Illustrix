import tensorflow as tf
import numpy as np
import cv2
from tensorflow.keras.models import Model

from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure

graph = tf.Graph()
with graph.as_default():
    model = tf.keras.models.load_model(file_structure.MODEL_FOLDER + "unet_jun.h5")

def background_remove_fun(file_name: str, system_file_path: str) -> str:
    with graph.as_default():
        image = cv2.imread(system_file_path, cv2.IMREAD_COLOR)
        bg_remove_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.BACKGROUND_REMOVE_PATH + system_file_path.split("/")[-1]
        removed_bg_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.USER_BACKGROUND_PATH + system_file_path.split("/")[-1]
        print(image.shape)
        original_image = image
        h, w, _ = image.shape
        image = cv2.resize(image, (256, 256))
        image = image/255.0
        image = image.astype(np.float32)
        image = np.expand_dims(image, axis=0)
        pred_mask = model.predict(image)[0]
        pred_mask = cv2.resize(pred_mask, (w, h))
        pred_mask = np.expand_dims(pred_mask, axis=-1)
        pred_mask = pred_mask > 0.5
        background_mask = np.abs(1- pred_mask)
        masked_image = original_image * pred_mask
        background_mask = np.concatenate([background_mask, background_mask, background_mask], axis=-1)
        background_mask = background_mask * [0, 0, 0]
        masked_image = masked_image + background_mask
        save_to_sub_folder(bg_remove_path, masked_image)
        save_to_sub_folder(removed_bg_path, original_image)
        save_to_final_folder(system_file_path, masked_image)
        return system_file_path
