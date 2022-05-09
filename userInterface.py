# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers
# Description: File to handle the UI for the imageClassiferDriver file

# Import libraries necessary for making UI
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
        # Variables for imgNum widget
        self.CurrentImgNum = 0
        self.maxImgNum = 0
        # UI Widget Creation
        self.image = QLabel("Please upload an image")
        self.imageName = QLabel("")
        self.next = QPushButton("Next")
        self.previous = QPushButton("Previous")
        self.imgNum = QLabel(str(self.CurrentImgNum) + " of " + str(self.maxImgNum))
        self.classification = QLabel("Classification: " + "insert animal here")
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
        layout.addWidget(self.classification, 2, 4, 1, 1)
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
        # Background to widgets
        self.image.setAlignment(Qt.AlignCenter)
        self.imgNum.setAlignment(Qt.AlignCenter)
        self.classification.setStyleSheet("border: 1px solid black; background-color: white")
        self.imageName.setStyleSheet("border: 1px solid black; background-color: white")
        self.image.setStyleSheet("border: 1px solid black; background-color: white")
        self.imgNum.setStyleSheet("border: 1px solid black; background-color: white")
        self.endProcess.setStyleSheet("color: red;")
        self.clearImage.setStyleSheet("color: orange;")
    
    # Functions to provide actions to button clicks
    # Method that changes to the next image, image name, classification, and image number
    def nextAction(self):
        # Only increase if less than maximum number of images
        if self.CurrentImgNum < self.maxImgNum:
            # Increase image number and update the widget
            self.CurrentImgNum = self.CurrentImgNum + 1
            self.updateImgNum()

            # Changes to other widgets needs to be added

        
        print("1")

    # Method that changes to the previous image, image name, classification, and image number
    def previousAction(self):
        # Only decrease if larger than 1
        if self.CurrentImgNum > 1:
            # Decrease image number and update widget
            self.CurrentImgNum = self.CurrentImgNum - 1
            self.updateImgNum()

            # Changes to other widgets needs to be added

        print("2")

    def infoButtonAction(self):
        print("3")

    # When upload is clicked, prompt to select a image then send it to imageClassifier
    def uploadAction(self):
        # Get path to file
        path = QFileDialog.getOpenFileName(None, "Select Image", "", "*.jpg *.png")
        
        # Only perform actions if a path was selected
        if path[0] != "":
            # Set image from path
            self.image.setPixmap(pix(path[0]).scaled(550, 550, Qt.KeepAspectRatio, Qt.FastTransformation))
            
            # Set image name from path
            self.imageName.setText(os.path.basename(path[0]))
    
            # Send path to imageClassifier
            """
            Comment needs to be removed when method is created
            imageClassifier.setFile(path[0])
            """
            print(path[0])
    
            # Set max number of images and update widget
            self.CurrentImgNum = 1
            self.maxImgNum = 1
            self.updateImgNum()




    def folderUploadAction(self):
        # Get path to folder
        path = QFileDialog.getExistingDirectory(None, "Choose Folder", "")
        
        # Only perform actions if a path was selected
        if path != "":
            """
            Comment needs to be removed when method is created
            imageClassifier.setFolder(path)

            # Set the number of files in the folder to the maxImgNum
            numFiles = imageClassifier.getNumFiles(path)
            self.maxImgNum = numFiles
            """
            # Remove maxImgNum = 1000 when above comment is uncommented
            self.maxImgNum = 1000
            self.updateImgNum()
            self.image.setText("Folder was uploaded, future image preview will go here")

            print(path)


    # When clear button is pressed, reset labels and image
    def clearImageAction(self):
        self.imageName.setText("")
        self.classification.setText("Classification:                          ")
        self.imgNum.setText("0 of 0")
        self.image.setPixmap(pix(""))
        self.image.setText("Please upload an image")


    def endProcessAction(self):
        """
        Comment needs to be removed when method is created
        imageClassifier.continueClassification(False)
        """
        print("7")

    def archiveAction(self):
        print("8")

    # Method to update the image numbers
    def updateImgNum(self):
        self.imgNum.setText(str(self.CurrentImgNum) + " of " + str(self.maxImgNum))