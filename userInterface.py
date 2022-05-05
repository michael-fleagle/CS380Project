# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers
# Description: File to handle the UI for the imageClassiferDriver file

# Import libraries necessary for making UI
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QLabel, QLineEdit, QGridLayout, QMessageBox,
                             QScrollArea, QFrame, QFileDialog)
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import QPixmap

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
        self.next.clicked.connect(self.nextAction)
        self.previous.clicked.connect(self.previousAction)
        self.infoButton.clicked.connect(self.infoButtonAction)
        self.upload.clicked.connect(self.uploadAction)
        self.folderUpload.clicked.connect(self.folderUploadAction)
        self.clearImage.clicked.connect(self.clearImageAction)
        self.endProcess.clicked.connect(self.endProcessAction)
        self.archive.clicked.connect(self.archiveAction)

        # Design
        # Add borders to widgets
        self.classification.setStyleSheet("border: 1px solid black;")
        self.imageName.setStyleSheet("border: 1px solid black;")
        self.image.setStyleSheet("border: 1px solid black;")
        self.pageNum.setStyleSheet("border: 1px solid black;")

    
    # Functions to provide actions to button clicks
    def nextAction(self):
        print("1")

    def previousAction(self):
        print("2")

    def infoButtonAction(self):
        print("3")

    # When upload is clicked, prompt to select a image then send it to imageClassifier
    def uploadAction(self):
        path = QFileDialog.getOpenFileName(None, "Select Image", "", "*.jpg *.png")
        self.image.setPixmap(QPixmap(path[0]).scaled(500, 500, Qt.KeepAspectRatio, Qt.FastTransformation))
        # Comment needs to be removed when method is created
        # imageClassifier.setFile(path[0])
        print(path[0])

    def folderUploadAction(self):
        path = QFileDialog.getExistingDirectory(None, "Choose Folder", "")
        # Comment needs to be removed when method is created
        # imageClassifier.setFolder(path)
        print(path)

    # Problem referencing method in class above
    def clearImageAction(self):
        self.imageName.setText("")
        self.classification.setText("Classification: ")
        self.pageNum.setText("0 of 0")


    def endProcessAction(self):
        # Comment needs to be removed when method is created
        # imageClassifier.continueClassification(False)
        print("7")

    def archiveAction(self):
        print("8")
