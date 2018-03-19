# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'url2qr.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QRView = QtWidgets.QGraphicsView(self.centralwidget)
        self.QRView.setObjectName("QRView")
        self.verticalLayout.addWidget(self.QRView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUrl.setText("")
        self.inputUrl.setClearButtonEnabled(False)
        self.inputUrl.setObjectName("inputUrl")
        self.horizontalLayout.addWidget(self.inputUrl)
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setObjectName("Button")
        self.horizontalLayout.addWidget(self.Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.Button.clicked.connect(self.click_button)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text to QRCode"))
        self.Button.setText(_translate("MainWindow", "ConvertQR!"))

    def click_button(self, MainWindow):
        text = self.inputUrl.text()
        if text == "":
            text = "https://google.co.jp/"
        scene = QtWidgets.QGraphicsScene()
        img = qrcode.make(text)
        item = QtWidgets.QGraphicsPixmapItem(img._img.toqpixmap())
        scene.addItem(item)
        self.QRView.setScene(scene)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
