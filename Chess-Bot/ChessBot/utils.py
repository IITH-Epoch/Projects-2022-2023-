import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential, Functional, Model, load_model
from keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
from PIL import Image
import subprocess
import itertools
import os
import shutil
import random
import glob
import matplotlib.pyplot as plt
from os import listdir
from keras.applications import imagenet_utils
import cv2
import warnings
from keras.preprocessing import image
warnings.simplefilter(action='ignore', category=FutureWarning)

m = ['a','b','c','d','e','f','g','h']

PATH_TO_MODEL = 'ChessPieceDetection/model.h5'
model = load_model(PATH_TO_MODEL)

def crop_img(path_to_image):
    img = cv2.imread(path_to_image)
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    img = cv2.resize(img, (512, 512))
    img = img[43:362, 60:480]
    img = cv2.resize(img, (512, 512))
    out = []
    for i in range(8):
        temp = []
        for j in range(8):
            temp.append(img[i*64:(i+1)*64,j*64:(j+1)*64])
        out.append(temp)
    return out

def get_array(path_to_photo):
    # 5 dimensional array of 64x(size of one cropped image)
    imgs = crop_img(path_to_photo)
    li = ['B', 'a', 'W']
    for i in range(8):
        for j in range(8):
            imgs[i][j] = Image.fromarray(imgs[i][j].astype('uint8'), 'RGB')
            imgs[i][j] = imgs[i][j].resize((224, 224))
            imgs[i][j] = tf.keras.applications.mobilenet.preprocess_input(np.array(imgs[i][j], dtype=np.float32))
            imgs[i][j] = np.expand_dims(imgs[i][j], axis=0)
    arr = [[li[model.predict(imgs[i][j])] for j in range(8)] for i in range(8)]
    # for i in range(8):
    #     temp = []
    #     for j in range(8):
    #         temp.append(model.predict(imgs[i][j]))
    #     arr.append(temp)
    return arr

def click_photo():
    subprocess.call("rm -rf img/*", shell=True)
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    # show result
    if result:

        # showing result, it take frame name and image
        # output
        cv2.imshow("img", image)

        # saving image in local storage
        cv2.imwrite("imgs/1.png", image)

        # If keyboard interrupt occurs, destroy image
        # window
        cv2.waitKey(10)
        cv2.destroyWindow("img")

    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

def move_from_player(arr, prev):
    changes = []
    ct = 0
    for i in range(8):
        for j in range(8):
            if (arr[i][j] != prev[i][j]):
                # s = f"{chr(j+'a')}{i+1}"
                changes.append([i,j])
                ct += 1
    # print(changes)
    move = ""
    if (ct==2):
        # One of the filled becomes empty and one of the empty becomes filled
        if (prev[changes[0][0]][changes[0][1]] =='a' and arr[changes[1][0]][changes[1][1]] != 'a'):
            move = f"{m[changes[0][1]]}{changes[0][0]+1}{m[changes[1][1]]}{changes[1][0]+1}"
        elif (prev[changes[0][0]][changes[0][1]] !='a' and arr[changes[1][0]][changes[1][1]] == 'a'):
            move = f"{m[changes[1][1]]}{changes[1][0]+1}{m[changes[0][1]]}{changes[0][0]+1}"
        # One of the filled becomes empty and one of the filled becomes filled with another filled
        else:
            if (arr[changes[0][0]][changes[0][1]] == 'a'):
                move = f"{m[changes[0][1]]}{changes[0][0]+1}{m[changes[1][1]]}{changes[1][0]+1}"
            else:
                move = f"{m[changes[1][1]]}{changes[1][0]+1}{m[changes[0][1]]}{changes[0][0]+1}"
    else:
        # Just one move needed
        move = f"{m[changes[0][1]]}{changes[0][0]+1}{m[changes[2][1]]}{changes[2][0]+1}"
        # move.append(f"{m[changes[3][1]]}{changes[3][0]+1}{m[changes[1][1]]}{changes[1][0]+1}")
    return move

def update_array(arr, move):
    temp = str(move)
    # print(temp)
    arr[int(temp[3])-1][ord(temp[2])-ord('a')] = arr[int(temp[1])-1][ord(temp[0])-ord('a')]
    arr[int(temp[1])-1][ord(temp[0])-ord('a')] = 'a'
    return arr