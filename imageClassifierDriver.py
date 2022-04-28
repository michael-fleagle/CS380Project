# Authors: Michael Fleagle, Kyah Fukunaga, Roman Kalabovda, Jacob Rogers
# Description: Driver file for the imageClassifier program

# Import all files
import userInterface
# import imageClassifier

from PyQt5.QtWidgets import QApplication
import sys

def winCreate():
    app = QApplication(sys.argv)
    # Create Window
    win = userInterface.LandingPage()
    win.show()

    sys.exit(app.exec_())
    
winCreate()