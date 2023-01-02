import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
import cv2

def preprocess(image):
    if (type(image) == Image.Image): img_arr = np.array(image.convert('L').resize((28,28))).reshape((28,28,1))
    elif (type(image) == np.ndarray): img_arr = np.invert(cv2.resize(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY),(28,28),interpolation=cv2.INTER_AREA).reshape((28,28,1)))
    img_arr = cv2.equalizeHist(img_arr)
    img_arr = img_arr.astype("float64")/255.0
    img_arr = np.array([img_arr])
    return img_arr

def predict(image):
    model = keras.models.load_model("./src/myModel.h5")
    img = preprocess(image)
    # cv2.imwrite("./src/out.jpg",255*img.reshape((28,28)))
    output = np.argmax(model(img))
    max = np.max(model(img))
    return (output,max)
