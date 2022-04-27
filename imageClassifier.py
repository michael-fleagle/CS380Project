# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers

#Import libraries necessary for image processing, 

import numpy as np
import tensorflow
import PIL
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# create a path to data directory
# must be changed for each user
img_dir = "I:\\CS 380\\Project\\CS380Project\\archive\\Animal"

# train animal directory
train_dir = os.path.join(img_dir, "train")

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
plt.show()
