# -*- coding: utf-8 -*-
import qdarkstyle
# Form implementation generated from reading ui file 'message.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from daysearch import get_message, start


class Ui_Message(QMainWindow):
    def __init__(self):
        super(Ui_Message,self).__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.get_text)
        self.show()
    def get_text(self):
        user=self.textEdit.toPlainText()
        password=self.linEdit_2.text()
        uid=self.textEdit_3.toPlainText()
        get_message(user,password,uid)
        self.close()
    def setupUi(self, Message):
        Message.setObjectName("Message")
        Message.resize(465, 265)
        self.label_2 = QtWidgets.QLabel(Message)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 141, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Message)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 141, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Message)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(Message)
        self.loginButton.setGeometry(QtCore.QRect(160, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.textEdit = QtWidgets.QTextEdit(Message)
        self.textEdit.setGeometry(QtCore.QRect(160, 30, 271, 41))
        self.textEdit.setObjectName("textEdit")
        # self.textEdit_2 = QtWidgets.QTextEdit(Message)
        # self.textEdit_2.setGeometry(QtCore.QRect(160, 100, 271, 41))
        # self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Message)
        self.textEdit_3.setGeometry(QtCore.QRect(160, 170, 271, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.linEdit_2=QtWidgets.QLineEdit(Message)
        self.linEdit_2.setGeometry(QtCore.QRect(160, 100, 271, 41))
        self.linEdit_2.setEchoMode(QLineEdit.Password)
        self.linEdit_2.setObjectName("lineEdit_2")
        self.retranslateUi(Message)
        QtCore.QMetaObject.connectSlotsByName(Message)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())  # 主题
        self.setWindowOpacity(0.9)  # 设置透明度
    def retranslateUi(self, Message):
        _translate = QtCore.QCoreApplication.translate
        Message.setWindowTitle(_translate("Message", "未响应正常,请勿关闭"))
        self.label_2.setText(_translate("Message", "密码"))
        self.label_3.setText(_translate("Message", "UID"))
        self.label.setText(_translate("Message", "用户名"))
        self.loginButton.setText(_translate("Message", "提交"))