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
        self.image = QLabel("Image will go here")
        self.imageName = QLabel("Name of Image")
        self.next = QPushButton("Next")
        self.previous = QPushButton("Previous")
        self.pageNum = QLabel("1 of 1")
        self.classification = QLabel("Classification: " + "insert animal here")
        self.infoButton = QPushButton("More Info")
        self.upload = QPushButton("Upload")
        self.folderUpload = QPushButton("Upload Folder")
        self.clearImage = QPushButton("Clear Image")
        self.endProcess = QPushButton("End Classification")
        self.archive = QPushButton("Archive")
        
        # Needs to be changed
        spacer = QLabel("")
        
        #create layout
        layout = QGridLayout()
        # addWidget(Name, Row, Col)
        # addWidget(Name, Row, Col, RowSpan, ColSpan)
        layout.addWidget(self.image, 2, 1, 3, 3)
        layout.addWidget(self.imageName, 1, 1, 1, 3)
        layout.addWidget(self.next, 5, 3)
        layout.addWidget(self.previous, 5, 1)
        layout.addWidget(self.pageNum, 5, 2)
        layout.addWidget(self.classification, 2, 4, 1, 1)
        layout.addWidget(self.infoButton, 3, 4, 1, 1)
        layout.addWidget(self.upload, 2, 5)
        layout.addWidget(self.folderUpload, 2, 6)
        layout.addWidget(self.clearImage, 3, 5)
        layout.addWidget(self.endProcess, 3, 6)
        layout.addWidget(self.archive, 4, 6)

        # Spacer widget - plan to change in the future
        layout.addWidget(spacer, 10, 1, 1, 6)

        # Set the layout as the layout
        self.setLayout(layout)

        # Calls to functions for button functionality
        self.next.clicked.connect(nextAction)
        self.previous.clicked.connect(previousAction)
        self.infoButton.clicked.connect(infoButtonAction)
        self.upload.clicked.connect(uploadAction)
        self.folderUpload.clicked.connect(folderUploadAction)
        self.clearImage.clicked.connect(clearImageAction)
        self.endProcess.clicked.connect(endProcessAction)
        self.archive.clicked.connect(archiveAction)

        # Design
        # Add borders to widgets
        self.classification.setStyleSheet("border: 1px solid black;")
        self.imageName.setStyleSheet("border: 1px solid black;")
        self.image.setStyleSheet("border: 1px solid black;")
        self.pageNum.setStyleSheet("border: 1px solid black;")

    # Setter and Getter Methods
    def setImgName(self):
        self.imageName.setText("Is This Working")


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
    LandingPage().setImgName()
    print("is this working????")
    
def endProcessAction():
    print("7")

def archiveAction():
    print("8")
