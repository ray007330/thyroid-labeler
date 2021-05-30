from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

import numpy as np
import pydicom


class QPaintLabel2(QLabel):
    def __init__(self, parent):
        super(QLabel, self).__init__(parent)
        self.dcm_image = None
        self.image = None
        self.imgr = None
        self.imgc = None
        
    def display_image(self):
        qformat = QImage.Format_Grayscale16
        w, h = self.width(), self.height()
        img = QImage(self.dcm_image, self.dcm_image.shape[1],
                     self.dcm_image.shape[0], qformat)
        backlash = self.lineWidth()*2
        self.setPixmap(QPixmap.fromImage(img).scaled(w-backlash, h-backlash, Qt.IgnoreAspectRatio))
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def load_dicom_image(self, fname):
        dcm = pydicom.dcmread(fname, force=True)
        dcm.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
        print(np.nanmax(dcm.pixel_array), np.nanmin(dcm.pixel_array))
        dcm.image = dcm.pixel_array * dcm.RescaleSlope + dcm.RescaleIntercept
        self.image = dcm.image.astype(np.uint8)
        self.dcm_image = self.image.copy()
        self.imgr, self.imgc = self.dcm_image.shape[0:2]
        self.display_image()