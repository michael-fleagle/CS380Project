# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers
# Description: File to handle the UI for the imageClassiferDriver file

# Import libraries necessary for making UI
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QLabel, QLineEdit, QGridLayout, QMessageBox,
                             QScrollArea, QFrame, QFileDialog)
from PyQt5.QtCore import (Qt)

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
        # UI Widget Creation
        image = QLabel("Image will go here")
        imageName = QLabel("Name of Image")
        next = QPushButton("Next")
        previous = QPushButton("Previous")
        pageNum = QLabel("1 of 1")
        classification = QLabel("Classification: " + "insert animal here")
        infoButton = QPushButton("More Info")
        upload = QPushButton("Upload")
        folderUpload = QPushButton("Upload Folder")
        clearImage = QPushButton("Clear Image")
        endProcess = QPushButton("End Classification")
        archive = QPushButton("Archive")
        
        spacer = QLabel("")
        
        #create layout
        layout = QGridLayout()
        # addWidget(Name, Row, Col)
        # addWidget(Name, Row, Col, RowSpan, ColSpan)
        layout.addWidget(image, 2, 1, 3, 3)
        layout.addWidget(imageName, 1, 1, 1, 3)
        layout.addWidget(next, 5, 3)
        layout.addWidget(previous, 5, 1)
        layout.addWidget(pageNum, 5, 2)
        layout.addWidget(classification, 2, 4, 1, 1)
        layout.addWidget(infoButton, 3, 4, 1, 1)
        layout.addWidget(upload, 2, 5)
        layout.addWidget(folderUpload, 2, 6)
        layout.addWidget(clearImage, 3, 5)
        layout.addWidget(endProcess, 3, 6)
        layout.addWidget(archive, 4, 6)

        # Spacer widget - plan to change in the future
        layout.addWidget(spacer, 10, 1, 1, 6)

        # Set the layout as the layout
        self.setLayout(layout)

        # Calls to functions for button functionality
        next.clicked.connect(nextAction)
        previous.clicked.connect(previousAction)
        infoButton.clicked.connect(infoButtonAction)
        upload.clicked.connect(uploadAction)
        folderUpload.clicked.connect(folderUploadAction)
        clearImage.clicked.connect(clearImageAction)
        endProcess.clicked.connect(endProcessAction)
        archive.clicked.connect(archiveAction)



        # Design
        # Add borders to widgets
        classification.setStyleSheet("border: 1px solid black;")
        imageName.setStyleSheet("border: 1px solid black;")
        image.setStyleSheet("border: 1px solid black;")
        pageNum.setStyleSheet("border: 1px solid black;")


# Functions to provide actions to button clicks
def nextAction():
    print("1")

def previousAction():
    print("2")

def infoButtonAction():
    print("3")

def uploadAction():
    path = QFileDialog.getOpenFileName(None, "Select Image", "", "*.jpg *.png")
    print(path)
    print(path[0])

def folderUploadAction():
    path = QFileDialog.getExistingDirectory(None, "Choose Folder", "")
    print(path)

def clearImageAction():
    print("6")

def endProcessAction():
    print("7")

def archiveAction():
    print("8")
