# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers
# Description: File to handle the UI for the imageClassiferDriver file

# Import libraries necessary for making UI
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QLabel, QLineEdit, QGridLayout, QMessageBox,
                             QScrollArea, QFrame)
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
        # Image Box
        image = QLabel("Image will go here")
        imageName = QLabel("Name of Image")
        next = QPushButton("Next")
        previous = QPushButton("Previous")
        pageNum = QLabel("1 of 1")
        info = QLabel("Info")
        upload = QPushButton("Upload")
        folderUpload = QPushButton("Upload Folder")
        clearImage = QPushButton("Clear Image")
        endProcess = QPushButton("End Classification")
        archive = QPushButton("Archive")
        
        spacer = QLabel("")
        
        #create layout
        layout = QGridLayout()
        # addWidget(Name, Row, Col, RowSpan, ColSpan)
        layout.addWidget(image, 2, 1, 3, 3)
        layout.addWidget(imageName, 1, 1, 1, 3)
        layout.addWidget(next, 5, 3)
        layout.addWidget(previous, 5, 1)
        layout.addWidget(pageNum, 5, 2)
        layout.addWidget(info, 2, 4, 3, 1)
        layout.addWidget(upload, 2, 5)
        layout.addWidget(folderUpload, 2, 6)
        layout.addWidget(clearImage, 3, 5)
        layout.addWidget(endProcess, 3, 6)
        layout.addWidget(archive, 4, 6)

        layout.addWidget(spacer, 10, 1, 1, 6)

        # Add borders to widgets
        info.setStyleSheet("border: 1px solid black;")
        imageName.setStyleSheet("border: 1px solid black;")
        image.setStyleSheet("border: 1px solid black;")
        pageNum.setStyleSheet("border: 1px solid black;")


        self.setLayout(layout)
        
        
