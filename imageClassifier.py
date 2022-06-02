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
# model.save('model')

# Change 'model' to the exact filepath where your model is saved
model = tf.keras.models.load_model('model')

# Variable for setFile to check to continue
continueClassification = True

# Recieves image path from userInterface, classifies image
def setFile(path):
    test_image = image.load_img(path, target_size=(200,200))

    # convert image to numpy array
    images = image.img_to_array(test_image)
    # expand dimension of image
    images = np.expand_dims(images, axis=0)
    # making prediction with model
    prediction = model.predict(images)
    
    print('Prediction: ')
    
    print(prediction)
    
    if prediction == 3:
        print('Cat')
        return "Cat"
    elif prediction == 4:
      print('Dog')
      return "Dog"
    elif prediction == 0:
      print('Elephant')
      return "Elephant"
    elif prediction == 1:
      print('Horse')
      return "Horse"
    elif prediction == 2:
      print('Lion')
      return "Lion"


# Method to classify a folder of images
def setFolder(dir, fileNames):
  if continueClassification:
    # List to append classifications to
    classification = []

    # For each file in the given directory, classify it and add it to list of classifications
    for file in fileNames:
      fullPath = dir + "/" + file
      classification.append(setFile(fullPath))

    # Return classifications as a tuple
    return tuple(classification)

# Method for setFile to check to stop
def stopClassification():
  continueClassification = False
