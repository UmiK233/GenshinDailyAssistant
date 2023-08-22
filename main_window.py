# -*- coding: utf-8 -*-
import qdarkstyle
# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from login_window import *
from daysearch import *
from message import *


class Ui_Dialog(object):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(379, 379)
        Dialog.setBaseSize(QtCore.QSize(6, 9))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setWindowOpacity(1.0)
        Dialog.setAutoFillBackground(True)
        Dialog.setModal(False)
        self.refreshButton = QtWidgets.QPushButton(Dialog)
        self.refreshButton.setGeometry(QtCore.QRect(0, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.refreshButton.setFont(font)
        self.refreshButton.setObjectName("refreshButton")
        self.minButton = QtWidgets.QPushButton(Dialog)
        self.minButton.setGeometry(QtCore.QRect(240, 0, 61, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.minButton.setFont(font)
        self.minButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.minButton.setObjectName("minButton")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(310, 0, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 0, 141, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(160, 100, 171, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 90, 61, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/task/uiimg/task.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 230, 51, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/sz/uiimg/shuzhi.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(160, 230, 171, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 310, 371, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.closeButton.clicked.connect(QApplication.quit)
        self.minButton.clicked.connect(self.minimize_to_tray)
        self.closeButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.minButton.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())  # 主题
        self.setWindowOpacity(0.9)  # 设置透明度
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.gologin)
        self.refreshButton.clicked.connect(self.refresh)

    def refresh(self):
        try:
            open('./message.txt', 'r', encoding='utf8')
        except:
            self.gomessage()
        try:
            list = start()
            _translate = QtCore.QCoreApplication.translate
            self.label_4.setText(_translate("Dialog", f"{list[0]}/4"))
            self.label_5.setText(_translate("Dialog", f"{list[1]}/160"))
            if list[2] == "None":
                self.label_3.setText(_translate("Dialog", "None"))
            else:
                if list[2]:
                    self.label_3.setText(_translate("Dialog", "今日委托奖励已领取"))
                else:
                    self.label_3.setText(_translate("Dialog", "今日委托奖励未领取"))
        except:
            pass

    def gomessage(self):
        self.window = Ui_Form()

    def gologin(self):
        self.window = Ui_Message()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "玩原神玩的"))
        self.refreshButton.setText(_translate("Dialog", "刷新"))
        self.minButton.setText(_translate("Dialog", "-"))
        self.closeButton.setText(_translate("Dialog", "X"))
        self.pushButton.setText(_translate("Dialog", "获取登录信息"))
        self.label_4.setText(_translate("Dialog", "None/4"))
        self.label_5.setText(_translate("Dialog", "None/160"))
        self.label_3.setText(_translate("Dialog", "None"))