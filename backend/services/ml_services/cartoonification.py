import cv2
import numpy as np
import os

import tensorflow.compat.v1  as tf1
tf1.disable_eager_execution()

import services.ml_services.network as network
import services.ml_services.guided_filter as guided_filter


from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure

input_photo = tf1.placeholder(tf1.float32, [1, None, None, 3])
network_out = network.unet_generator(input_photo)
final_out = guided_filter.guided_filter(input_photo, network_out, r=1, eps=5e-3)
all_vars = tf1.trainable_variables()
gene_vars = [var for var in all_vars if 'generator' in var.name]
saver = tf1.train.Saver(var_list=gene_vars)
config = tf1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf1.Session(config=config)
sess.run(tf1.global_variables_initializer())
saver.restore(sess, tf1.train.latest_checkpoint(file_structure.CARTOONIFICATION_MODEL))

def resize_crop(image):
    h, w, c = np.shape(image)
    if min(h, w) > 720:
        if h > w:
            h, w = int(720*h/w), 720
        else:
            h, w = 720, int(720*w/h)
    image = cv2.resize(image, (w, h),
                       interpolation=cv2.INTER_AREA)
    h, w = (h//8)*8, (w//8)*8
    image = image[:h, :w, :]
    return image

def cartoonification_fun(file_name: str, system_file_path: str, factor: int) -> str:
    try:
        image = cv2.imread(system_file_path)
        image = resize_crop(image)
        batch_image = image.astype(np.float32)/127.5 - 1
        batch_image = np.expand_dims(batch_image, axis=0)
        output = sess.run(final_out, feed_dict={input_photo: batch_image})
        output = (np.squeeze(output)+1)*127.5
        cartoonification_output = np.clip(output, 0, 255).astype(np.uint8)
        cartoonification_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.CARTOONNIFICATION_PATH + system_file_path.split("/")[-1]
        save_to_sub_folder(cartoonification_path, cartoonification_output)
        save_to_final_folder(system_file_path, cartoonification_output)
    except Exception as e:
        print("edjke",e)
        print(e.__traceback__.tb_lineno)
    return system_file_path