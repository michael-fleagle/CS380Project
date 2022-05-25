# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers

#Import libraries necessary for image processing, 

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import PIL
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Saves the model from training
model.save('model')
model = tf.keras.models.load_model('model')

# Recieves image path from userInterface, classifies image
def setFile(path):
    test_image = image.load_img(path, target_size=(200,200))

    # convert image to numpy array
    images = image.img_to_array(test_image)
    # expand dimension of image
    images = np.expand_dims(images, axis=0)
    # making prediction with model
    prediction = model.predict(images)
    
    if prediction == 0:
        print('Cat')
    elif prediction == 1:
      print('Dog')
    elif prediction == 2:
      print('Elephant')
    elif prediction == 3:
      print('Horse')
    elif prediction == 4:
      print('Lion')
