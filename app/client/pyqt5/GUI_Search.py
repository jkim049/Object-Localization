import os
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from PyQt5.uic.properties import QtCore
from pyqtgraph.Qt import QtCore

from server.Video import Video


class GUI_Search(QDialog):
    def __init__(self, parent = None):
        super(GUI_Search, self).__init__(parent)

        # LOAD UI FROM .UI FILE (FROM QT DESIGNER)
        loadUi('./client/GUI_Search.ui', self)


        self.button_search.clicked.connect(self.search)

        self.checkBox_searchRed.stateChanged.connect(self.searchRed_state_changed)
        self.checkBox_searchGreen.stateChanged.connect(self.searchGreen_state_changed)
        self.checkBox_searchBlue.stateChanged.connect(self.searchBlue_state_changed)
        self.checkBox_searchYellow.stateChanged.connect(self.searchYellow_state_changed)

        # INITIALIZE CHECK BOX
        self.searchRed = False
        self.searchGreen = False
        self.searchBlue = False
        self.searchYellow = False
        self.checkBox_searchRed.setChecked(self.searchRed)
        self.checkBox_searchGreen.setChecked(self.searchGreen)
        self.checkBox_searchBlue.setChecked(self.searchBlue)
        self.checkBox_searchYellow.setChecked(self.searchYellow)

        # CHECK BOX LISTENERS
        self.checkBox_searchRed.stateChanged.connect(self.searchRed_state_changed)
        self.checkBox_searchGreen.stateChanged.connect(self.searchGreen_state_changed)
        self.checkBox_searchBlue.stateChanged.connect(self.searchBlue_state_changed)
        self.checkBox_searchYellow.stateChanged.connect(self.searchYellow_state_changed)

        # DATE/TIME PICKERS
        # get current date and time
        now = QtCore.QDateTime.currentDateTime()
        self.dateTimeEdit_searchFrom.setDateTime(now)
        self.dateTimeEdit_searchTo.setDateTime(now)


    def searchRed_state_changed(self):
        """ Monitor when search red checkbox is checked/unchecked """
        try:
            if self.checkBox_searchRed.isChecked():
                self.searchRed = True
            else:
                self.searchRed = False
            return
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)

    def searchGreen_state_changed(self):
        """ Monitor when search green checkbox is checked/unchecked """
        try:
            if self.checkBox_searchGreen.isChecked():
                self.searchGreen = True
            else:
                self.searchGreen = False
            return
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)

    def searchBlue_state_changed(self):
        """ Monitor when search blue checkbox is checked/unchecked """
        try:
            if self.checkBox_searchBlue.isChecked():
                self.searchBlue = True
            else:
                self.searchBlue = False
            return
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)

    def searchYellow_state_changed(self):
        """ Monitor when search yellow checkbox is checked/unchecked """
        try:
            if self.checkBox_searchYellow.isChecked():
                self.searchYellow = True
            else:
                self.searchYellow = False

            return
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)

    def get_dateTimeEdit_searchFrom(self):
        try:
            year = self.dateTimeEdit_searchFrom.date().year()

            month = self.dateTimeEdit_searchFrom.date().month()
            if (month < 10):
                month = "0" + str(month)

            day = self.dateTimeEdit_searchFrom.date().day()
            if (day < 10):
                day = "0" + str(day)

            searchFrom = "{year}-{month}-{day}".format(year=str(year), month=str(month), day=str(day))

            return searchFrom

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)

    def get_dateTimeEdit_searchTo(self):
        try:
            year = self.dateTimeEdit_searchTo.date().year()

            month = self.dateTimeEdit_searchTo.date().month()
            if (month < 10):
                month = "0" + str(month)

            day = self.dateTimeEdit_searchTo.date().day()
            if (day < 10):
                day = "0" + str(day)

            searchTo = "{year}-{month}-{day}".format(year=str(year), month=str(month), day=str(day))

            return searchTo
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)

    def search(self):

        # CREATE and CONNECT to DATABASE
        # self.db = Database.Database()
        # self.db.connect()
        # filename = self.db.get(self.searchRed, self.searchGreen,
        #                         self.searchBlue, self.searchYellow,
        #                         self.get_dateTimeEdit_searchFrom(),
        #                         self.get_dateTimeEdit_searchTo(),
        #                         self.textEdit_searchVideoName.toPlainText())
        self.v0 = Video("0")
        #if(filename is not None):
        self.v0.setVidSource("./videos/green-blue-yellow.avi")

        self.timer0 = QTimer(self)
        self.timer0.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer0.timeout.connect(lambda: self.update_frame(self.v0))
        self.timer0.start()


    def update_frame(self, video):
        """ Update frame for specific video """
        try:
            ret, video.frame = video.vidCap.read()
            self.display_frame(video.frame, 0, 1)

            return

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)

    def display_frame(self, _frame, source, window=1):
        """ Display frame for specific video """
        try:
            print("displaying")
            qformat = QImage.Format_RGB888
            if len(_frame.shape) == 3:
                if _frame.shape[2] == 4:
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888

            outputImage = QImage(_frame, _frame.shape[1], _frame.shape[0], _frame.strides[0], qformat)
            outputImage = outputImage.rgbSwapped()

            if window == 1:
                if source == 0:
                    self.label_searchVideo0.setPixmap(QPixmap.fromImage(outputImage))
                    self.label_searchVideo0.setScaledContents(True)
                elif source == 1:
                    self.label_searchVideo1.setPixmap(QPixmap.fromImage(outputImage))
                    self.label_searchVideo1.setScaledContents(True)
                elif source == 2:
                    self.label_searchVideo2.setPixmap(QPixmap.fromImage(outputImage))
                    self.label_searchVideo2.setScaledContents(True)
            return

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(e)