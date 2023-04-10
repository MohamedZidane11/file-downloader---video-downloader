# import PyQt5 Library
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

# import Sys, Os, Path Library
import sys
import os
from os import path

# import Ui File
ui,_ = loadUiType('main.ui')


# initiate Ui File
class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)





def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show() # Show the app window
    app.exec_() # Infinite loop

if __name__ == '__main__':
    main()