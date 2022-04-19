from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from  PyQt5.uic import loadUiType
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("giphy.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(5, 0, 931, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("T8bahf.gif"))
        self.label_3.setObjectName("label_3")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 890, 100, 85))
        self.pushButton.setStyleSheet("font: 63 16pt \"Yu Gothic UI Semibold\";\n"
                                      "border-color: rgb(255, 255, 127);\n"
                                      "background-color: rgb(54, 255, 23);\n"
                                      "border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 890, 100, 85))
        self.pushButton_2.setStyleSheet("font: 63 16pt \"Yu Gothic UI Semibold\";\n"
                                        "background-color: rgb(255, 7, 27);")
        self.pushButton_2.setObjectName("pushButton_2")

        #self.label_4 = QtWidgets.QLabel(self.centralwidget)
        #self.label_4.setGeometry(QtCore.QRect(1340, 810, 521, 261))
        #self.label_4.setText("")
        #self.label_4.setPixmap(QtGui.QPixmap("run (4).gif"))
        #self.label_4.setScaledContents(True)
        #self.label_4.setObjectName("label_4")
        #self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        #self.textBrowser.setGeometry(QtCore.QRect(1000, 10, 216, 42))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        #self.textBrowser.setFont(font)
        #self.textBrowser.setStyleSheet("background-color:trnsparant;\n"
#"border-radius:none;\n"
#"color:white;\n"
#"font-size:20px;")
        #self.textBrowser.setObjectName("textBrowser")
        #self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        #self.textBrowser_2.setGeometry(QtCore.QRect(1000, 10, 216, 42))
        #font = QtGui.QFont()
        #font.setFamily("Nirmala UI")
        #font.setPointSize(16)
        #font.setBold(True)
        #font.setWeight(75)
        #self.textBrowser_2.setFont(font)
        #self.textBrowser_2.setStyleSheet("background-color: trnsparant;\n"
#border-radius:none;"
#"color:white;\n"
#"font-size:20px;")
        #self.textBrowser_2.setObjectName("textBrowser_2")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.pushButton.setText(_translate("mainWindow", "RUN"))
        self.pushButton_2.setText(_translate("mainWindow", "EXIT"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())



