# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent
from PyQt5.QtWidgets import QDialog, QFileDialog, QGraphicsScene
from PyQt5.uic import loadUi
import os
import numpy as np
import pydicom
import utils
import cv2

class Ui_Dialog(QDialog):
    def __init__(self, Dialog):
        super().__init__()
        path = os.getcwd()
        print(path)
        os.chdir(path)
        loadUi('labeler.ui', self)

        Dialog.setObjectName("Thyroid-Labeler")
        Dialog.resize(1129, 698)
        self.draw = QtWidgets.QPushButton(Dialog)
        self.draw.setGeometry(QtCore.QRect(710, 620, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.draw.setFont(font)
        self.draw.setObjectName("draw")
        self.reset = QtWidgets.QPushButton(Dialog)
        self.reset.setGeometry(QtCore.QRect(790, 620, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(310, 590, 371, 61))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 30, 381, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(570, 30, 381, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.openfile_1 = QtWidgets.QPushButton(Dialog)
        self.openfile_1.setGeometry(QtCore.QRect(410, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.openfile_1.setFont(font)
        self.openfile_1.setObjectName("openfile_1")
        self.openfile_2 = QtWidgets.QPushButton(Dialog)
        self.openfile_2.setGeometry(QtCore.QRect(960, 30, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.openfile_2.setFont(font)
        self.openfile_2.setObjectName("openfile_2")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(20, 130, 1081, 411))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.splitter)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.splitter)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.cropsave = QtWidgets.QPushButton(Dialog)
        self.cropsave.setGeometry(QtCore.QRect(1000, 620, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.cropsave.setFont(font)
        self.cropsave.setObjectName("cropsave")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(710, 580, 361, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 100, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(790, 100, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.scene1 = QGraphicsScene()
        self.scene2 = QGraphicsScene()

        self.graphicsView_3.mousePressEvent = self.selectPoints
        self.retranslateUi(Dialog)
        self.positions = []
        self.reset.clicked.connect(lambda: self.clearPoints())
        self.draw.clicked.connect(lambda: self.drawRect())
        self.cropsave.clicked.connect(lambda: self.saveCrop())
        self.w_ratio = 0
        self.h_ratio = 0
        self.save_dir_path = ''

        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.openfile_1.clicked.connect(lambda: self.load_clicked(1))
        self.openfile_2.clicked.connect(lambda: self.load_clicked(2))
        self.dcm_image_1 = None
        self.dcm_image_2 = None
        self.image = None
        # self.imgr = None
        # self.imgc = None



    def load_clicked(self, subwindow):
        print("clicked!")
        fname, _filter = QFileDialog.getOpenFileName(self, 'open file', '~/Desktop')
        if subwindow == 1:
            self.load_dicom_image(fname, 1)
            print(fname)
            self.textBrowser.clear()
            self.textBrowser.append(fname)
            self.graphicsView_3.setScene(self.scene1)
            self.graphicsView_3.show()
        elif subwindow == 2:
            self.load_dicom_image(fname, 2)
            print(fname)
            self.textBrowser_2.clear()
            self.textBrowser_2.append(fname)
            self.graphicsView_4.setScene(self.scene2)
            self.graphicsView_4.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Thyroid-Labeler"))
        self.draw.setText(_translate("Dialog", "draw"))
        self.reset.setText(_translate("Dialog", "reset"))
        self.openfile_1.setText(_translate("Dialog", "openfile"))
        self.openfile_2.setText(_translate("Dialog", "openfile"))
        self.cropsave.setText(_translate("Dialog", "save"))
        self.label.setText(_translate("Dialog", "reference view"))
        self.label_2.setText(_translate("Dialog", "original view"))

    def display_image(self, scene):
        qformat = QImage.Format_RGB888
        if scene == 1:
            image = self.dcm_image_1
            view = self.graphicsView_3
            scene = self.scene1
        elif scene == 2:
            image = self.dcm_image_2
            view = self.graphicsView_4
            scene = self.scene2
        w, h = view.width(), view.height()
        img = QImage(image, image.shape[1],
                     image.shape[0], qformat)
        backlash = view.lineWidth()*2
        self.w_ratio = image.shape[1]/(w-backlash)
        self.h_ratio = image.shape[0]/(h-backlash)
        scene.addPixmap(QPixmap.fromImage(img).scaled(w-backlash, h-backlash, QtCore.Qt.IgnoreAspectRatio))
        view.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def load_dicom_image(self, fname, scene):
        dcm = pydicom.dcmread(fname, force=True)
        # print(np.nanmax(dcm.pixel_array), np.nanmin(dcm.pixel_array))
        self.image = dcm.pixel_array.astype(np.uint8)
        if scene == 1:
            self.dcm_image_1 = np.stack((self.image,)*3, axis=-1)
        # default save dir
        if scene == 2:
            self.dcm_image_2 = np.stack((self.image,)*3, axis=-1)
            self.dcm = dcm
            save_dir, self.dcm_fname = fname.split('/')[:-1], fname.split('/')[-1]
            self.textEdit_2.setPlainText('/'.join(save_dir)+"/"+dcm.PatientID)
        # self.imgr, self.imgc = self.dcm_image.shape[0:2]
        self.display_image(scene)

    def selectPoints(self,  event):
        pos_x = event.pos().x()
        pos_y = event.pos().y()
        print(str(pos_x)+' '+str(pos_y))
        self.positions.append(str(pos_x))
        self.positions.append(str(pos_y))
        self.textEdit.setPlainText(' '.join(self.positions))

    def clearPoints(self):
        self.positions = []
        self.textEdit.clear()

    def drawRect(self):
        # print(self.dcm_image.shape)
        # print(self.w_ratio)
        # print(self.h_ratio)
        if len(self.positions)==4:
            x1 = int(self.positions[0])
            y1 = int(self.positions[1])
            x2 = int(self.positions[2])
            y2 = int(self.positions[3])
            new_img = np.copy(self.dcm_image_2)
            view = self.graphicsView_4
            scene = self.scene2
            w, h = view.width(), view.height()
            backlash = view.lineWidth()*2
            cv2.rectangle(new_img, (int(x1*self.w_ratio), int(y1*self.h_ratio)), (int(x2*self.w_ratio), int(y2*self.h_ratio)), (255, 0, 0), 2)
            new_img = QImage(new_img, self.dcm_image_2.shape[1],
                     self.dcm_image_2.shape[0], QImage.Format_RGB888)
            scene.addPixmap(QPixmap.fromImage(new_img).scaled(w-backlash, h-backlash, QtCore.Qt.IgnoreAspectRatio))
            view.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    def saveCrop(self):
        if len(self.positions)==4:
            x1 = int(self.positions[0])
            y1 = int(self.positions[1])
            x2 = int(self.positions[2])
            y2 = int(self.positions[3])
            if x1 > x2:
                t = x2
                x2 = x1
                x1 = t
            if y1 > y2:
                t = y2
                y2 = y1
                y1 = t
            path = self.textEdit_2.toPlainText()
            print(path)

            if os.path.isdir(path):
                for root, dirs, files in os.walk(path, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                os.rmdir(path)
                print("remove older folder...")

            os.mkdir(path)
            os.chdir(path)
            self.dcm.save_as(self.dcm_fname)
            suffix = '.npy'
            # deal with crop
            crop_img = self.dcm_image_2[int(y1*self.h_ratio):int(y2*self.h_ratio), int(x1*self.w_ratio):int(x2*self.w_ratio)]
            # cv2.imshow('tt', crop_img)
            # save original image numpy and crop image
            with open(self.dcm_fname+suffix, 'wb') as f:
                np.save(f, self.dcm_image_2)
            with open('crop.npy', 'wb') as f:
                np.save(f, crop_img)
            # save positions
            with open('positions.txt', 'w') as f:
                f.write(' '.join([str(int(x1*self.w_ratio)), str(int(y1*self.h_ratio)), str(int(x2*self.w_ratio)), str(int(y2*self.h_ratio))]))
            print('Saving files succeed!')


         

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
