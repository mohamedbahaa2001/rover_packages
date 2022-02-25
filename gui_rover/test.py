# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from re import S
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from threading import Thread
import time
import sys
  
minute = 15
second = 00

class Ui_MainWindow(object):
    flag = 1
    time_in_minutes = minute
    time_in_second = second
    def addZero(self,timeInSecond):
        if timeInSecond < 10:
            return '0' + str(timeInSecond)
        else:
            return str(timeInSecond)
    def update_gui(self):
        # if self.time_in_second < 10:
        #     self.timerValueLbl.setText(str(f"{self.time_in_minutes} : {self.addZero(self.time_in_second)}"))
        # else:
        self.timerValueLbl.setText(str(f"{self.time_in_minutes} : {self.addZero(self.time_in_second)}"))

    def timer_timeout(self):
        if self.time_in_second == 0:
            self.time_in_minutes = self.time_in_minutes - 1
            self.time_in_second = 60
        self.time_in_second = self.time_in_second - 1
        self.update_gui()
    def startTimerFunc(self):
        if self.flag == 1:
            self.time_in_minutes = minute
            self.time_in_second = second
            self.flag = 0
        self.timer = QtCore.QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timer_timeout)

        # self.timerValueLbl.setText(str(f"{self.min} : {self.sec}"))
        # self.timerValueLbl.setText(QTime.minute(self.min).toString() + " : " + QTime.second(self.sec).toString())
        
        
        # while(True):
        #     self.timerValueLbl.setText(str(f"{self.min} : {self.min}"))

        #     if self.sec == 0:
        #         self.min = self.min - 1
        #         self.sec = 60
        #     self.sec = self.sec - 1
        #     print("min: " + str(self.min) + ' sec: ' + str(self.sec))
        #     time.sleep(1)
        #     if self.min == 0 and self.sec == 0:
        #         break
        #     print(QTime.currentTime().toString())
        # def stopTimerFunc(self):
        #     self.timer.stop()
        #     self.timerValueLbl.setText(str(f"{self.min} : {self.sec}"))

        # self.timerValueLbl.setText(str(int(self.timerValueLbl.text()) - 1))
    def stopTimerFunc(self):
        self.timer.stop()
        self.timerValueLbl.setText(str(f"{self.time_in_minutes} : {self.addZero(self.time_in_second)}"))
    def resetTimerFunc(self):
        self.time_in_minutes = minute
        self.time_in_second = second
        self.update_gui()
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(983, 732)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 190, 371, 241))
        self.groupBox.setMinimumSize(QtCore.QSize(281, 241))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.motor6Label = QtWidgets.QLabel(self.groupBox)
        self.motor6Label.setMinimumSize(QtCore.QSize(58, 17))
        self.motor6Label.setObjectName("motor6Label")
        self.gridLayout_3.addWidget(self.motor6Label, 10, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 3, 0, 1, 1)
        self.motor1Label = QtWidgets.QLabel(self.groupBox)
        self.motor1Label.setMinimumSize(QtCore.QSize(62, 17))
        self.motor1Label.setObjectName("motor1Label")
        self.gridLayout_3.addWidget(self.motor1Label, 0, 0, 1, 1)
        self.motor3Label = QtWidgets.QLabel(self.groupBox)
        self.motor3Label.setMinimumSize(QtCore.QSize(58, 17))
        self.motor3Label.setObjectName("motor3Label")
        self.gridLayout_3.addWidget(self.motor3Label, 4, 0, 1, 1)
        self.motor5Label = QtWidgets.QLabel(self.groupBox)
        self.motor5Label.setMinimumSize(QtCore.QSize(58, 17))
        self.motor5Label.setObjectName("motor5Label")
        self.gridLayout_3.addWidget(self.motor5Label, 8, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.groupBox)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 7, 0, 1, 1)
        self.motor2Label = QtWidgets.QLabel(self.groupBox)
        self.motor2Label.setMinimumSize(QtCore.QSize(58, 17))
        self.motor2Label.setObjectName("motor2Label")
        self.gridLayout_3.addWidget(self.motor2Label, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 9, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 5, 0, 1, 1)
        self.motor4Label = QtWidgets.QLabel(self.groupBox)
        self.motor4Label.setMinimumSize(QtCore.QSize(58, 17))
        self.motor4Label.setObjectName("motor4Label")
        self.gridLayout_3.addWidget(self.motor4Label, 6, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setEnabled(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_3.addWidget(self.textEdit_2, 2, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_3.addWidget(self.textEdit_3, 4, 1, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_3.addWidget(self.textEdit_4, 6, 1, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_3.addWidget(self.textEdit_5, 8, 1, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_6.setEnabled(False)
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout_3.addWidget(self.textEdit_6, 10, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 440, 441, 241))
        self.groupBox_3.setMinimumSize(QtCore.QSize(281, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buriedLabel = QtWidgets.QLabel(self.groupBox_3)
        self.buriedLabel.setMinimumSize(QtCore.QSize(58, 17))
        self.buriedLabel.setObjectName("buriedLabel")
        self.gridLayout_4.addWidget(self.buriedLabel, 6, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.groupBox_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_4.addWidget(self.line_7, 1, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.groupBox_3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_4.addWidget(self.line_10, 5, 0, 1, 1)
        self.surfaceLabel = QtWidgets.QLabel(self.groupBox_3)
        self.surfaceLabel.setMinimumSize(QtCore.QSize(58, 17))
        self.surfaceLabel.setObjectName("surfaceLabel")
        self.gridLayout_4.addWidget(self.surfaceLabel, 8, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.groupBox_3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_4.addWidget(self.line_9, 7, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.groupBox_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_4.addWidget(self.line_8, 3, 0, 1, 1)
        self.velocityLabel = QtWidgets.QLabel(self.groupBox_3)
        self.velocityLabel.setMinimumSize(QtCore.QSize(62, 17))
        self.velocityLabel.setObjectName("velocityLabel")
        self.gridLayout_4.addWidget(self.velocityLabel, 0, 0, 1, 1)
        self.minedetectorlabel = QtWidgets.QLabel(self.groupBox_3)
        self.minedetectorlabel.setMinimumSize(QtCore.QSize(58, 17))
        self.minedetectorlabel.setObjectName("minedetectorlabel")
        self.gridLayout_4.addWidget(self.minedetectorlabel, 4, 0, 1, 1)
        self.gyroscopeLabel = QtWidgets.QLabel(self.groupBox_3)
        self.gyroscopeLabel.setMinimumSize(QtCore.QSize(58, 17))
        self.gyroscopeLabel.setObjectName("gyroscopeLabel")
        self.gridLayout_4.addWidget(self.gyroscopeLabel, 2, 0, 1, 1)
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_7.setEnabled(False)
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout_4.addWidget(self.textEdit_7, 0, 1, 1, 1)
        self.textEdit_8 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_8.setEnabled(False)
        self.textEdit_8.setObjectName("textEdit_8")
        self.gridLayout_4.addWidget(self.textEdit_8, 2, 1, 1, 1)
        self.textEdit_9 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_9.setEnabled(False)
        self.textEdit_9.setObjectName("textEdit_9")
        self.gridLayout_4.addWidget(self.textEdit_9, 4, 1, 1, 1)
        self.textEdit_10 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_10.setEnabled(False)
        self.textEdit_10.setObjectName("textEdit_10")
        self.gridLayout_4.addWidget(self.textEdit_10, 6, 1, 1, 1)
        self.textEdit_11 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_11.setEnabled(False)
        self.textEdit_11.setObjectName("textEdit_11")
        self.gridLayout_4.addWidget(self.textEdit_11, 8, 1, 1, 1)
        self.surfaceMapTable = QtWidgets.QTableView(self.centralwidget)
        self.surfaceMapTable.setGeometry(QtCore.QRect(730, 120, 241, 481))
        self.surfaceMapTable.setObjectName("surfaceMapTable")
        self.buridMapTable = QtWidgets.QTableView(self.centralwidget)
        self.buridMapTable.setGeometry(QtCore.QRect(480, 120, 241, 481))
        self.buridMapTable.setObjectName("buridMapTable")
        self.showDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showDataBtn.setGeometry(QtCore.QRect(670, 610, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.showDataBtn.setFont(font)
        self.showDataBtn.setAutoDefault(False)
        self.showDataBtn.setObjectName("showDataBtn")
        self.timerlbl = QtWidgets.QLabel(self.centralwidget)
        self.timerlbl.setGeometry(QtCore.QRect(20, 40, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.timerlbl.setFont(font)
        self.timerlbl.setObjectName("timerlbl")
        self.surfaceMineMaplbl = QtWidgets.QLabel(self.centralwidget)
        self.surfaceMineMaplbl.setGeometry(QtCore.QRect(760, 70, 191, 41))
        self.surfaceMineMaplbl.setTextFormat(QtCore.Qt.RichText)
        self.surfaceMineMaplbl.setObjectName("surfaceMineMaplbl")
        self.buridMineMaplbl = QtWidgets.QLabel(self.centralwidget)
        self.buridMineMaplbl.setGeometry(QtCore.QRect(510, 70, 191, 41))
        self.buridMineMaplbl.setTextFormat(QtCore.Qt.RichText)
        self.buridMineMaplbl.setObjectName("buridMineMaplbl")
        self.timerValueLbl = QtWidgets.QLabel(self.centralwidget)
        self.timerValueLbl.setGeometry(QtCore.QRect(110, 40, 81, 17))
        self.timerValueLbl.setObjectName("timerValueLbl")
        self.timerValueLbl.setText(str(f"{self.time_in_minutes} : {self.addZero(self.time_in_second)}"))

        
        self.startTimer = QtWidgets.QPushButton(self.centralwidget)
        self.startTimer.setGeometry(QtCore.QRect(20, 90, 121, 31))
        self.startTimer.setObjectName("startTimer")
        self.startTimer.clicked.connect(self.startTimerFunc)

        self.stopTimer = QtWidgets.QPushButton(self.centralwidget)
        self.stopTimer.setGeometry(QtCore.QRect(150, 90, 121, 31))
        self.stopTimer.setObjectName("stopTimer")
        self.stopTimer.clicked.connect(self.stopTimerFunc)
        self.resetTimer = QtWidgets.QPushButton(self.centralwidget)
        self.resetTimer.setGeometry(QtCore.QRect(90, 130, 121, 31))
        self.resetTimer.setObjectName("resetTimer")
        self.resetTimer.clicked.connect(self.resetTimerFunc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 983, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Motors Speed"))
        self.motor6Label.setText(_translate("MainWindow", "Motor 6:"))
        self.motor1Label.setText(_translate("MainWindow", "Motor 1: "))
        self.motor3Label.setText(_translate("MainWindow", "Motor 3:"))
        self.motor5Label.setText(_translate("MainWindow", "Motor 5:"))
        self.motor2Label.setText(_translate("MainWindow", "Motor 2:"))
        self.motor4Label.setText(_translate("MainWindow", "Motor 4:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sensors and functions"))
        self.buriedLabel.setText(_translate("MainWindow", "Buried mines"))
        self.surfaceLabel.setText(_translate("MainWindow", "Surface mines"))
        self.velocityLabel.setText(_translate("MainWindow", "Velocity"))
        self.minedetectorlabel.setText(_translate("MainWindow", "Mine Detectore state"))
        self.gyroscopeLabel.setText(_translate("MainWindow", "Gyroscope"))
        self.showDataBtn.setText(_translate("MainWindow", "Show Maps"))
        self.timerlbl.setText(_translate("MainWindow", "Timer:"))
        self.surfaceMineMaplbl.setText(_translate("MainWindow", "Surface vector map"))
        self.buridMineMaplbl.setText(_translate("MainWindow", "Buried vector map"))
        self.timerValueLbl.setText(_translate("MainWindow", str(f"{self.time_in_minutes} : {self.addZero(self.time_in_second)}")))
        self.startTimer.setText(_translate("MainWindow", "Start"))
        self.stopTimer.setText(_translate("MainWindow", "Stop"))
        self.resetTimer.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())