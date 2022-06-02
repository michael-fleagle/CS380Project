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

train = False
test = False

if train == True:
    # create a path to data directory
    # must be changed for each user
    img_dir = "I:\\CS 380\\Project\\CS380Project\\archive\\Animal"
    # img_dir = "D:\\Animal" # Used for Jacob's laptop

    # train animal directory
    train_dir = os.path.join(img_dir, "train")
    # validation animal directory
    val_dir = os.path.join(img_dir, 'val')

    # Use os to create a proper file path
    trainCatDir = os.path.join(train_dir, "cat")
    trainDogDir = os.path.join(train_dir, "dog")
    trainElDir = os.path.join(train_dir, "elephant")
    trainHorDir = os.path.join(train_dir, "horse")
    trainLioDir = os.path.join(train_dir, "lion")

    # Create list of image names from directory
    trainCatNames = os.listdir(trainCatDir)
    trainDogNames = os.listdir(trainDogDir)
    trainElNames = os.listdir(trainElDir)
    trainHorNames = os.listdir(trainHorDir)
    trainLioNames = os.listdir(trainLioDir)

    # Data Preprocessing and Augmentation
    # Generate training, testing and validation batches
    dgen_train = ImageDataGenerator(rescale=1./255,
                                    validation_split=0.2,  # use 20% of training data for validation 
                                    zoom_range=0.2,
                                    horizontal_flip=True)
    dgen_validation = ImageDataGenerator(rescale=1./255)
    dgen_test = ImageDataGenerator(rescale=1./255)

    TARGET_SIZE = (200, 200)
    BATCH_SIZE = 64
    CLASS_MODE = 'categorical'

    # Connecting the ImageDataGenerator objects to our dataset
    train_generator = dgen_train.flow_from_directory(train_dir,
                                                    target_size=TARGET_SIZE,
                                                    subset='training',
                                                    batch_size=BATCH_SIZE,
                                                    class_mode=CLASS_MODE)

    validation_generator = dgen_train.flow_from_directory(val_dir,
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
    model.add(Dense(5, activation='softmax'))
    model.summary()

    # Compile the Model
    model.compile(Adam(lr=0.001), loss='categorical_crossentropy', metrics = ['accuracy'])

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

# Tests to evaluate the model. Delete once effective model found.
if test == True:
    # Testing model
    valPath = 'I:/CS 380/Project/CS380Project/archive/Animal/val/'
    testPath = 'I:\CS 380\Project\Local Version\TestingData'
    newFig = plt.figure(figsize=(20, 20))

    # labels = os.listdir(valPath)

    batchHolder = np.zeros((25, 200, 200, 3))

    
    for i,img in enumerate(os.listdir(testPath)):
        img = image.load_img(os.path.join(os.path.join(testPath, img)), target_size=(200,200))
        batchHolder[i, :] = img

    model = tf.keras.models.load_model('I:\CS 380\Project\CS380Project\model\model_ 0.897')
    prediction = model.predict_classes(batchHolder)

    for i,img in enumerate(batchHolder):
        newFig.add_subplot(5, 5, i + 1)
        plt.title(prediction[i][0])
        plt.imshow(img/256.)

    plt.show()
    
