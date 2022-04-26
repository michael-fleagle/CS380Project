# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers

#Import libraries necessary for image processing, 

import numpy as np
import tensorflow
import PIL
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# create a path to data directory
img_dir = "\archive" # Should this be "\\archive"? 
# I believe that only having one backslash causes the a to interpret it as a special character

# train animal directory
# must be changed for each user
train_cat = "I:/CS 380/Project/CS380Project/archive/Animal/train/cat"
train_dog = "I:/CS 380/Project/CS380Project/archive/Animal/train/dog"
train_eleph = "I:/CS 380/Project/CS380Project/archive/Animal/train/ELEPHANT"
train_horse = "I:/CS 380/Project/CS380Project/archive/Animal/train/HORSE"
train_lion = "I:/CS 380/Project/CS380Project/archive/Animal/train/LION"

# Use os to create a proper file path
trainCatDir = os.path.join(train_cat)
trainDogDir = os.path.join(train_dog)
trainElDir = os.path.join(train_eleph)
trainHorDir = os.path.join(train_horse)
trainLioDir = os.path.join(train_lion)

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
    data = imgPath.split('/', 6)[6]
    
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


# Testing fix to git