import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # Disables the warning
# Libraries
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.datasets import mnist
import numpy as np

def CNN_Model(x_train) :
    input = keras.Input(shape=(x_train.shape[1],x_train.shape[2],x_train.shape[3]))
    x = layers.Conv2D(20,5,activation="relu")(input)
    x = layers.MaxPool2D()(x)
    x = layers.Conv2D(40,5,activation="relu")(x)
    x = layers.MaxPool2D()(x)
    x = layers.Flatten()(x)
    x = layers.Dense(64,activation="relu")(x)
    output = layers.Dense(10,activation="softmax")(x)
    model = keras.Model(inputs=input,outputs= output)
    model.compile( 
        loss = keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        optimizer=keras.optimizers.Adam(lr=0.001),
        metrics=["accuracy"]
    )
    return model

def CreateModel():
    (x_train,y_train),(x_test,y_test) = mnist.load_data()


    image_gen = ImageDataGenerator(width_shift_range=0.1, 
                                height_shift_range=0.1, 
                                shear_range=0.1, 
                                zoom_range=0.2, 
                                horizontal_flip=False,
                                vertical_flip=False,
                                fill_mode='nearest')  

    # Normalize the data between [0,1]
    x_train = x_train.reshape((-1,x_train.shape[1],x_train.shape[2],1)).astype("float64")/255.0
    x_test = x_test.reshape((-1,x_test.shape[1],x_test.shape[2],1)).astype("float64")/255.0

    image_gen.fit(x_train)

    model = CNN_Model(x_train)
    model.fit(image_gen.flow(x_train,y_train),batch_size=10,epochs=3,verbose=1)
    model.save("./src/myModel.h5")
    model.evaluate(x_test,y_test)
