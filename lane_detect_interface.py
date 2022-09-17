
from email.mime import image
from signal import Signals
from sre_parse import State
import sys
import pandas as pd

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal
  
import datetime
import cv2
import time
import os
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

import torch
from fastai.vision.all import *
import cv2
import pandas as pd
import cv2
import numpy as np
import time


from model import model_line
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    global img
    def run(self):
        # cap = cv2.VideoCapture('C:\\Users\\oozer\\Desktop\\Driver state\\driver_test_video.mp4')#****************152******************
        # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # out = cv2.VideoWriter('D:\\omar\\plaka\\output.mp4', fourcc, 20.0, (2688,1520))
        cap = cv2.VideoCapture('C:\\Users\\omer\\Desktop\\LAne detection\\vide2.mp4')#****************152******************'C:\\Users\\ozer\\Desktop\\LAne detection\\road.MP4'
        
        # cap = cv2.VideoCapture('videoplayback.mp4')
        while True:
            ret, frame = cap.read()
            
            if ret:
                # out.write(frame) 
                
                
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                resized = cv2.resize(frame, (640,480))
                self.img=resized
                self.changePixmap.emit(p)
                cv2.waitKey(10)
                # cv2.waitKey(25)#for video
        #     else:
        #         break
        # out.release()
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys

class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)

      
        self.state='C:\\Users\\omer\\Desktop\\LAne detection\\pred.png'
        self.acceptDrops()
        # set the title
        self.setWindowTitle("Pred Image")
 
        # setting  the geometry of window
        self.setGeometry(0, 0, 640, 480)
 
        # creating label
        self.label = QLabel(self)
         
        # loading image
        self.pixmap = QPixmap(self.state)
 
        # adding image to label
        self.label.setPixmap(self.pixmap)
 
        # Optional, resize label to image size
        # self.label.resize(self.pixmap.width(),
        #                   self.pixmap.height())
        self.label.resize(1024,
                          720)
        # show all the widgets
        self.show()
 
class App(QMainWindow):
    global save_con
    save_con=False
    def __init__(self):
        super().__init__()
        self.title = 'Lane detection'
        self.text='***Demo***'
        self.left = 50
        self.top = 50
        self.width = 500
        self.height = 200
        self.dialogs = list()
        # self.setCentralWidget(self.table)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QLabel(self)
        self.label.move(280, 120)
        self.label.resize(640, 480)
        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.start()
        # Create textbox
        # self.textbox = QLineEdit(self.text,self)
        # self.textbox.move(20, 20)
        # self.textbox.resize(280,40)
        # self.text='Koluman Plaka Tanıma Sistemi'
        self.textbox = QLineEdit(self.text,self)
        self.textbox.move(550, 600)
        self.textbox.resize(280,40)
        f = self.textbox.font()
        f.setPointSize(14) # sets the size to 27
        self.textbox.setFont(f)
        
        

       


        self.button = QPushButton('Run', self)
        self.button.move(350,600)
        f3=self.button.font()
        f3.setPointSize(14) # sets the size to 27
        self.button.setFont(f3)
        self.button.resize(175,50)
        self.button.clicked.connect(self.on_click_save)
        
        
        self.show()
        
    

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
        

    @pyqtSlot()
    def on_click_save(self):
        
        
        original_image_path=f'C:\\Users\\omer\\Desktop\\LAne detection\\test_video\\image_.png'
        self.th.changePixmap.disconnect(self.setImage)
        cv2.imwrite(original_image_path,self.th.img)
        
        
        state=model_line()
        
        # self.label = QLabel(self)
         
        # # loading image
        # self.pixmap = QPixmap(state)
 
        # # adding image to label
        # self.label.setPixmap(self.pixmap)
        dialog = Second(self)
        self.dialogs.append(dialog)
        dialog.state=state
        dialog.show()
        # self.th.changePixmap.connect(self.setImage)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
