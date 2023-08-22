from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QCursor, QIcon, QKeySequence
from PyQt5.QtWidgets import *
import sys
from daysearch import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from selenium import webdriver
import requests
from time import sleep
import requests
import hashlib
import math
import time
import random
import qdarkstyle
import pic
from login_window import *
from main_window import *
import ctypes


class Myexe(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self._restore_action = QAction()
        self._hide_action = QAction()
        self._quit_action = QAction()
        self._tray_icon_menu = QMenu()
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(":/ys/uiimg/ys.png"))  # 替换为你的图标路径
        self.tray_icon.setToolTip("原神每日小助手 By Umi")
        self.create_actions()
        self.create_tray_icon()
        self.tray_icon.show()
        self.tray_icon.activated[QSystemTrayIcon.ActivationReason].connect(self.iconActivated)

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def create_actions(self):
        # 创建菜单项
        self._restore_action = QAction("显示", self)
        self._restore_action.triggered.connect(self.restore_from_tray)  # "显示"菜单项触发还原窗口的操作
        self._hide_action = QAction("隐藏", self)
        self._hide_action.triggered.connect(self.minimize_to_tray)  # "显示"菜单项触发还原窗口的操作
        self._quit_action = QAction("退出", self)
        self._quit_action.triggered.connect(QApplication.quit)  # "退出"菜单项触发退出应用程序的操作

    def minimize_to_tray(self):
        # 最小化窗口到系统托盘
        self.hide()

    def listen_keyboard(self):
        # 键盘监听
        shortcut = QShortcut(QKeySequence("Esc"), self)
        # 当按下 Esc 键时隐藏窗口
        shortcut.activated.connect(self.hide)

    def create_tray_icon(self):
        # 创建系统托盘图标和上下文菜单
        self._tray_icon_menu = QMenu(self)
        self._tray_icon_menu.addAction(self._restore_action)
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._hide_action)
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._quit_action)
        self.tray_icon.setContextMenu(self._tray_icon_menu)
        self.tray_icon.show()

    def restore_from_tray(self):
        # 还原窗口
        if self.isMinimized():
            self.showNormal()
        elif self.isMaximized():
            self.showMaximized()
        else:
            self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/ys/uiimg/ys.png'))
    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    qt = Myexe()
    QApplication.setQuitOnLastWindowClosed(False)
    sys.exit(app.exec())
