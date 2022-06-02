# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers

# This file trains the neural network on the dataset and creates a model to be used for classification
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import PIL
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# create a path to data directory
# must be changed for each user
img_dir = "I:\\CS 380\\Project\\CS380Project\\archive\\Animal"
# img_dir = "D:\\Animal" # Used for Jacob's laptop

train_dir = os.path.join(img_dir, "train")


# Use os to create a proper file path
trainCatDir = os.path.join(train_dir, "cat")
trainDogDir = os.path.join(train_dir, "dog")
"""
trainElDir = os.path.join(train_dir, "elephant")
trainHorDir = os.path.join(train_dir, "horse")
trainLioDir = os.path.join(train_dir, "lion")
"""
# Create list of image names from directory
trainCatNames = os.listdir(trainCatDir)
trainDogNames = os.listdir(trainDogDir)

"""
trainElNames = os.listdir(trainElDir)
trainHorNames = os.listdir(trainHorDir)
trainLioNames = os.listdir(trainLioDir)
"""


ROWS = 4
COLS = 4

fig = plt.gcf()
fig.set_size_inches(12, 12)

# create 
catPic = [os.path.join(trainCatDir, filename) for filename in trainCatNames[:8]]

notCatPic = [os.path.join(trainDogDir, filename) for filename in trainDogNames[:8]]

# merge the cat and not cat pictures
mergeList = catPic + notCatPic

# Plot the images
for i, imgPath in enumerate(mergeList):
    #get filename
    data = imgPath.split('\\')
    data = data[len(data)-1]

    #create subplot of images with rows and cols
    subP = plt.subplot(ROWS, COLS, i+1)
    
    # turn off axis
    subP.axis('Off')
    
    # read image data into an array
    img = mpimg.imread(imgPath)
    
    #setting title of plot as the filename
    subP.set_title(data, fontsize=6)
    
    #display data as image
    plt.imshow(img, cmap='gray')
    
# display the plot
# plt.show()

# Data Preprocessing and Augmentation
# Generate training, testing and validation batches
dgen_train = ImageDataGenerator(rescale=1./255,
                                validation_split=0.2,  # using 20% of training data for validation 
                                zoom_range=0.2,
                                horizontal_flip=True)
dgen_validation = ImageDataGenerator(rescale=1./255)
dgen_test = ImageDataGenerator(rescale=1./255)

TARGET_SIZE = (200, 200)
BATCH_SIZE = 32
CLASS_MODE = 'binary'

# Connecting the ImageDataGenerator objects to our dataset
train_generator = dgen_train.flow_from_directory(train_dir,
                                                target_size=TARGET_SIZE,
                                                subset='training',
                                                batch_size=BATCH_SIZE,
                                                class_mode=CLASS_MODE)

validation_generator = dgen_train.flow_from_directory(train_dir,
                                                    target_size=TARGET_SIZE,
                                                    subset='validation',
                                                    batch_size=BATCH_SIZE,
                                                    class_mode=CLASS_MODE)

# Get the class indices
train_generator.class_indices

# Get the image shape
train_generator.image_shape

# Building CNN Model
model = Sequential()
model.add(Conv2D(32, (5,5), padding='same', activation='relu',
                input_shape=(200, 200, 3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(Conv2D(64, (5,5), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))
model.summary()

# Compile the Model
model.compile(Adam(lr=0.001), loss='binary_crossentropy', metrics = ['accuracy'])

# Train the model
modHist = model.fit(train_generator, 
                    epochs = 30,
                    validation_data = validation_generator,
                    callbacks = [
                        # stop training if accuracy does not improve
                        tf.keras.callbacks.EarlyStopping(monitor = 'val_accuracy', patience = 20),

                        # save weight and model
                        tf.keras.callbacks.ModelCheckpoint('model_{val_accuracy: .3f}',
                                                        save_best_only = True,
                                                        save_weights_only = False,
                                                        monitor = 'val_accuracy'
                                                        )
                                ]
                    )
