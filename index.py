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
        # program functions calling
        self.hand_ui()
        self.hand_buttons()

    # ---- ui editing function -----
    def hand_ui(self):
        self.setWindowTitle('PyQT Downloader')
        self.setFixedSize(800,600)


    # ----- file downloader main functions -----
    def hand_buttons(self):
        pass


    def hand_browse(self):
        pass


    def hand_progressBar(self):
        pass


    def download(self):
        pass



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show() # Show the app window
    app.exec_() # Infinite loop

if __name__ == '__main__':
    main()