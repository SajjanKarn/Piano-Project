# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piano.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pygame import mixer


mixer.init()

class Ui_MainWindow(object):
    
    def play_music(self, music_filename):
        mixer.music.load(music_filename)
        mixer.music.play()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 227)
        MainWindow.setStyleSheet("#btnC{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnD{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnE{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnF{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnG{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnH{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnI{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnJ{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnK{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnL{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnM{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnN{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"#btnO{\n"
"background-color: black;\n"
"color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1241, 221))
        self.frame.setStyleSheet("#frame{\n"
"background-color: white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnA = QtWidgets.QPushButton(self.frame)
        self.btnA.setGeometry(QtCore.QRect(10, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnA.setFont(font)
        self.btnA.setStyleSheet("#btnA{\n"
"background-color: black;\n"
"color: white;\n"
"border: 1px solid white;\n"
"}")
        self.btnA.setObjectName("btnA")
        self.btnB = QtWidgets.QPushButton(self.frame)
        self.btnB.setGeometry(QtCore.QRect(80, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnB.setFont(font)
        self.btnB.setStyleSheet("#btnB{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"")
        self.btnB.setObjectName("btnB")
        self.btnC = QtWidgets.QPushButton(self.frame)
        self.btnC.setGeometry(QtCore.QRect(150, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnC.setFont(font)
        self.btnC.setObjectName("btnC")
        self.btnD = QtWidgets.QPushButton(self.frame)
        self.btnD.setGeometry(QtCore.QRect(220, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnD.setFont(font)
        self.btnD.setObjectName("btnD")
        self.btnE = QtWidgets.QPushButton(self.frame)
        self.btnE.setGeometry(QtCore.QRect(290, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnE.setFont(font)
        self.btnE.setStyleSheet("PushButton{\n"
"background-color: black;\n"
"border: none;\n"
"}")
        self.btnE.setObjectName("btnE")
        self.btnF = QtWidgets.QPushButton(self.frame)
        self.btnF.setGeometry(QtCore.QRect(360, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnF.setFont(font)
        self.btnF.setObjectName("btnF")
        self.btnG = QtWidgets.QPushButton(self.frame)
        self.btnG.setGeometry(QtCore.QRect(430, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnG.setFont(font)
        self.btnG.setObjectName("btnG")
        self.btnH = QtWidgets.QPushButton(self.frame)
        self.btnH.setGeometry(QtCore.QRect(500, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnH.setFont(font)
        self.btnH.setObjectName("btnH")
        self.btnI = QtWidgets.QPushButton(self.frame)
        self.btnI.setGeometry(QtCore.QRect(570, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnI.setFont(font)
        self.btnI.setObjectName("btnI")
        self.btnJ = QtWidgets.QPushButton(self.frame)
        self.btnJ.setGeometry(QtCore.QRect(640, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnJ.setFont(font)
        self.btnJ.setObjectName("btnJ")
        self.btnK = QtWidgets.QPushButton(self.frame)
        self.btnK.setGeometry(QtCore.QRect(710, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnK.setFont(font)
        self.btnK.setObjectName("btnK")
        self.btnL = QtWidgets.QPushButton(self.frame)
        self.btnL.setGeometry(QtCore.QRect(780, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnL.setFont(font)
        self.btnL.setObjectName("btnL")
        self.btnM = QtWidgets.QPushButton(self.frame)
        self.btnM.setGeometry(QtCore.QRect(850, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnM.setFont(font)
        self.btnM.setObjectName("btnM")
        self.btnN = QtWidgets.QPushButton(self.frame)
        self.btnN.setGeometry(QtCore.QRect(920, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnN.setFont(font)
        self.btnN.setObjectName("btnN")
        self.btnO = QtWidgets.QPushButton(self.frame)
        self.btnO.setGeometry(QtCore.QRect(990, 0, 61, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnO.setFont(font)
        self.btnO.setObjectName("btnO")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnA.clicked.connect(self.play_music("1.wav"))
        self.btnB.clicked.connect(self.play_music("2.wav"))
        self.btnC.clicked.connect(self.play_music("3.wav"))
        self.btnD.clicked.connect(self.play_music("4.wav"))
        self.btnE.clicked.connect(self.play_music("5.wav"))
        self.btnF.clicked.connect(self.play_music("6.wav"))
        self.btnG.clicked.connect(self.play_music("7.wav"))
        self.btnH.clicked.connect(self.play_music("8.wav"))
        self.btnI.clicked.connect(self.play_music("9.wav"))
        self.btnJ.clicked.connect(self.play_music("10.wav"))
        self.btnK.clicked.connect(self.play_music("11.wav"))
        self.btnL.clicked.connect(self.play_music("12.wav"))
        self.btnM.clicked.connect(self.play_music("13.wav"))
        self.btnN.clicked.connect(self.play_music("14.wav"))
        self.btnO.clicked.connect(self.play_music("15.wav"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Piano"))
        self.btnA.setText(_translate("MainWindow", "A"))
        self.btnB.setText(_translate("MainWindow", "B"))
        self.btnC.setText(_translate("MainWindow", "C"))
        self.btnD.setText(_translate("MainWindow", "D"))
        self.btnE.setText(_translate("MainWindow", "E"))
        self.btnF.setText(_translate("MainWindow", "F"))
        self.btnG.setText(_translate("MainWindow", "G"))
        self.btnH.setText(_translate("MainWindow", "H"))
        self.btnI.setText(_translate("MainWindow", "I"))
        self.btnJ.setText(_translate("MainWindow", "J"))
        self.btnK.setText(_translate("MainWindow", "K"))
        self.btnL.setText(_translate("MainWindow", "L"))
        self.btnM.setText(_translate("MainWindow", "M"))
        self.btnN.setText(_translate("MainWindow", "N"))
        self.btnO.setText(_translate("MainWindow", "O"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
