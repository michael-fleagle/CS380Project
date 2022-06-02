# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers
# Description: File to handle the UI for the imageClassiferDriver file

# Import libraries necessary for making UI
import imageClassifier
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QLabel, QLineEdit, QGridLayout, QMessageBox,
                             QScrollArea, QFrame, QFileDialog)
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import QPixmap as pix
import os

# CLass to create initial landing page
class LandingPage(QWidget):

    #intit method
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Image Classifier")
        self.resize(1000, 500)
        self.UiElem()

    # Method to create all UI elements for Landing page
    def UiElem(self):
        # Variable to hold path of file or folder
        self.filePath = ()
        self.dirPath = ""

        # Variables for imgNum widget
        self.currentImgNum = 0
        self.maxImgNum = 0

        # Variable to hold classifications
        self.classificationNames = ()
        
        # UI Widget Creation
        self.image = QLabel("Please upload an image")
        self.imageName = QLabel("")
        self.next = QPushButton("Next")
        self.previous = QPushButton("Previous")
        self.imgNum = QLabel(str(self.currentImgNum) + " of " + str(self.maxImgNum))
        self.classificationLabel = QLabel("Classification:                          ")
        self.infoButton = QPushButton("More Info")
        self.upload = QPushButton("Upload")
        self.folderUpload = QPushButton("Upload Folder")
        self.clearImage = QPushButton("Clear Image")
        self.endProcess = QPushButton("End Classification")
        self.archive = QPushButton("Archive")
        
        
        #create layout
        layout = QGridLayout()
        # addWidget(Name, Row, Col)
        # addWidget(Name, Row, Col, RowSpan, ColSpan)
        layout.addWidget(self.image, 2, 1, 5, 3)
        layout.addWidget(self.imageName, 1, 1, 1, 3)
        layout.addWidget(self.next, 7, 3)
        layout.addWidget(self.previous, 7, 1)
        layout.addWidget(self.imgNum, 7, 2)
        layout.addWidget(self.classificationLabel, 2, 4, 1, 1)
        layout.addWidget(self.infoButton, 3, 4, 1, 1)
        layout.addWidget(self.upload, 1, 6)
        layout.addWidget(self.folderUpload, 2, 6)
        layout.addWidget(self.clearImage, 3, 6)
        layout.addWidget(self.endProcess, 4, 6)
        layout.addWidget(self.archive, 5, 6)

        # Set the layout as the layout
        self.setLayout(layout)

        # Calls to functions for button functionality
        self.next.clicked.connect(self.nextAction)
        self.previous.clicked.connect(self.previousAction)
        self.infoButton.clicked.connect(self.infoButtonAction)
        self.upload.clicked.connect(self.uploadAction)
        self.folderUpload.clicked.connect(self.folderUploadAction)
        self.clearImage.clicked.connect(self.clearImageAction)
        self.endProcess.clicked.connect(self.endProcessAction)
        self.archive.clicked.connect(self.archiveAction)

        # Design
        # Text Alignment
        self.image.setAlignment(Qt.AlignCenter)
        self.imgNum.setAlignment(Qt.AlignCenter)
        self.imageName.setAlignment(Qt.AlignCenter)
        
        # Background to widgets
        self.classificationLabel.setStyleSheet("border: 1px solid black; background-color: white")
        self.imageName.setStyleSheet("border: 1px solid black; background-color: white")
        self.image.setStyleSheet("border: 1px solid black; background-color: white")
        self.imgNum.setStyleSheet("border: 1px solid black; background-color: white")
        
        # Text Color
        self.endProcess.setStyleSheet("color: red;")
        self.clearImage.setStyleSheet("color: orange;")
    
    # Functions to provide actions to button clicks
    # Method that changes to the next image, image name, classification, and image number
    def nextAction(self):
        # Only increase if less than maximum number of images
        if self.currentImgNum < self.maxImgNum:
            # Increase image number and update the widget
            self.currentImgNum = self.currentImgNum + 1
            self.updateImgNum()
            self.updateImgDisplay()
            self.updateImgName()
            self.updateClassification()

    # Method that changes to the previous image, image name, classification, and image number
    def previousAction(self):
        # Only decrease if larger than 1
        if self.currentImgNum > 1:
            # Decrease image number and update widget
            self.currentImgNum = self.currentImgNum - 1
            self.updateImgNum()
            self.updateImgDisplay()
            self.updateImgName()
            self.updateClassification()

    # Method to provide more info
    def infoButtonAction(self):

        classify = 'CAT'

        if classify is 'CAT':

            info = open('animal_info\\CAT.txt', 'r')
            message = info.read()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("More Information on Cats")
            msg.setText(message)
            msg.setStandardButtons(QMessageBox.Ok)
            

        if classify is 'DOG':

            info = open('animal_info\\DOG.txt', 'r')
            message = info.read()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("More Information on Dogs")
            msg.setText(message)
            msg.setStandardButtons(QMessageBox.Ok)

        if classify is 'ELEPHANT':

            info = open('animal_info\\ELEPHANT.txt', 'r')
            message = info.read()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("More Information on Elephants")
            msg.setText(message)
            msg.setStandardButtons(QMessageBox.Ok)
        
        if classify is 'HORSE':

            info = open('animal_info\\HORSE.txt', 'r')
            message = info.read()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("More Information on Horses")
            msg.setText(message)
            msg.setStandardButtons(QMessageBox.Ok)

        if classify is 'LION':

            info = open('animal_info\\LION.txt', 'r')
            message = info.read()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("More Information on Lions")
            msg.setText(message)
            msg.setStandardButtons(QMessageBox.Ok)

        msg.show()





    # When upload is clicked, prompt to select a image then send it to imageClassifier
    def uploadAction(self):
        # Get path to file
        pathTemp = QFileDialog.getOpenFileName(None, "Select Image", "", "*.jpg *.png")
        
        # Only perform actions if a path was selected
        if pathTemp[0] != "":
            
            # Send path to imageClassifier
            tempStr = imageClassifier.setFile(pathTemp[0])
            tempTuple = (tempStr, " ")
            self.classificationNames = tempTuple[:1]
            
            # Set the path variable to only the first part of the pathTemp
            self.filePath = (pathTemp[:1])
    
            # Set max number of images and update window
            self.currentImgNum = 1
            self.maxImgNum = 1
            self.updateImgNum()
            self.updateImgDisplay()
            self.updateImgName()
            self.updateClassification()

            # Reminder in console that this is not finished
            print(self.filePath)



    def folderUploadAction(self):
        # Get path to folder
        self.dirPath = QFileDialog.getExistingDirectory(None, "Choose Folder", "")
        
        # Only perform actions if a path was selected
        if self.dirPath != "":
            
            # Give processing feedback
            self.image.setText("Classifying... please wait")


            # Place the list of files in the folder into filePath
            self.filePath = self.fileFilter(self.dirPath)
            
            # Comment needs to be removed when method is created
            self.classificationNames = imageClassifier.setFolder(self.dirPath, self.filePath)
            
            # Set maxNum and reset currentNum and update window
            self.currentImgNum = 1
            self.maxImgNum = len(self.filePath)
            self.updateImgNum()
            self.updateImgDisplay()
            self.updateImgName()
            self.updateClassification()

            # Reminder in console that this is not finished
            # print(self.filePath)


    # When clear button is pressed, reset labels and image
    def clearImageAction(self):
        self.imageName.setText("")
        self.classificationLabel.setText("Classification:                          ")
        self.currentImgNum = 0
        self.maxImgNum = 0
        self.updateImgNum()
        self.image.setPixmap(pix(""))
        self.image.setText("Please upload an image")
        self.dirPath = ""
        self.filePath = ()


    def endProcessAction(self):
        
        # Set the check in imageClassifier.py to flase
        imageClassifier.stopClassification()
        
        print("7")

    def archiveAction(self):
        print("8")

    # Methods to update
    # Image numbers
    def updateImgNum(self):
        self.imgNum.setText(str(self.currentImgNum) + " of " + str(self.maxImgNum))

    # Image display
    def updateImgDisplay(self):
        # Set image from path based on currentImgNum
        index = self.currentImgNum - 1
        if self.dirPath == "":
            self.image.setPixmap(pix(self.filePath[index]).scaled(550, 550, Qt.KeepAspectRatio, Qt.FastTransformation))
        else:
            self.image.setPixmap(pix(self.dirPath + "/" + self.filePath[index]).scaled(550, 550, Qt.KeepAspectRatio, Qt.FastTransformation))

    # Image name
    def updateImgName(self):
        # Set Image name based on name of file at index of currentImgNum
        index = self.currentImgNum - 1
        self.imageName.setText(os.path.basename(self.filePath[index]))
        
    # Classifications
    def updateClassification(self):
        
        index = self.currentImgNum - 1
        self.classificationLabel.setText("Classification: " + self.classificationNames[index])
        
        # self.classificationLabel.setText("Classification: " + "                        ")

    # Method to filter out non png and jpg files from directory
    def fileFilter(self, path):
        allFiles = os.listdir(path)
        filtered = []
        
        # Loop through all the files and add png and jpg files to filtered
        for file in allFiles:
            if file.endswith(".png") or file.endswith(".jpg"):
                filtered.append(file)

        # Return the filtered list of files as tuple
        return tuple(filtered)