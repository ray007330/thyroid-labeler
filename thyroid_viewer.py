from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

import os 
import pydicom
import numpy as np



class CtwoD(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('labeler.ui', self)
        self.openfile_1.clicked.connect(self.load_clicked, 1)
        self.openfile_2.clicked.connect(self.load_clicked, 2)
        self.imgLabel_1.window = 1
        self.imgLabel_2.window = 2












    def load_clicked(self, subwindow):
        print("suck")
        fname, _filter = QFileDialog.getOpenFileName(self, 'open file', '~/Desktop',
                                                     "Image Files (*.dcm *DCM)")
        if subwindow == 1:
            self.imgLabel_1.load_dicom_image(fname)
        elif subwindow == 2:
            self.imgLabel_2.load_dicom_image(fname)





