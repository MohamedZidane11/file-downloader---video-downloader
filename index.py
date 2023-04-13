# import PyQt5 Library
import urllib.request

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

# import Sys, Os, Path Library
import sys
import os
from os import path

#import ytube library
import pafy
from humanize import naturalsize


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
        self.pushButton.clicked.connect(self.download_files)
        self.pushButton_2.clicked.connect(self.hand_browse)
        self.pushButton_3.clicked.connect(self.video_download)
        self.pushButton_7.clicked.connect(self.video_info)


    def hand_browse(self):
        save_place = QFileDialog.getSaveFileName(self, caption='Save As', directory='.', filter='All Files (*.*)')
        browse = str(save_place).split(',')[0][2:-1]
        self.lineEdit_2.setText(browse)


    def hand_progress(self, blocknum, blocksize, totalsize):
        read = blocknum * blocksize
        if totalsize > 0:
            percent = read * 100 / totalsize
            self.progressBar.setValue(percent)
            # Threading solution for not responding
            QApplication.processEvents()



    def download_files(self):
        # url - save location - progress
        url = self.lineEdit_1.text()
        save_location = self.lineEdit_2.text()
        #progress = ''

        try:
            urllib.request.urlretrieve(url, save_location, self.hand_progress)
        except Exception:
            QMessageBox.warning(self, 'Download Error', 'Download Failed :(')
            return
        QMessageBox.information(self, 'Download Completed', 'Download Finished :)')
        self.progressBar.setValue(0)
        self.lineEdit_1.setText('')
        self.lineEdit_2.setText('')

    # ----- youtube downloader main functions -----
    def video_info(self):
        link = self.lineEdit_4.text()
        v = pafy.new(f"{link}")
        all_streams = v.allstreams
        # print(v.title)
        # print(v.duration)
        # print(v.rating)
        # print("==============")
        # print(v.getbest().get_filesize())
        # print("==============")
        # print(v.author)
        # print(v.length)
        # # print(v.keywords)
        # print(v.thumb)
        # print(v.videoid)
        # print(v.viewcount)
        # print("==============")
        # print(v.allstreams)

        for s in all_streams:
            size = naturalsize(s.get_filesize())
            videos_data = '{} {} {} {}'.format(s.mediatype, s.extension, s.quality, s.resolution, size)
            self.comboBox.addItem(videos_data)
            # print(s.mediatype, s.extension, s.quality, s.resolution, size)


    def video_download(self):
        link = self.lineEdit_4.text()
        v = pafy.new(f"{link}")
        all_streams = v.allstreams
        vid_quality = ''
        vid_down = ''


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show() # Show the app window
    app.exec_() # Infinite loop

if __name__ == '__main__':
    main()