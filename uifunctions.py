from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMainWindow, QSizeGrip
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QColor
from client import *

class UIFunctions():
    def __init__(self,window : QMainWindow, chat_ui, connect_ui):
        self.window = window
        self.chat_ui = chat_ui
        self.connect_ui = connect_ui

    def ui_definitions(self):
        # REMOVING OS DEFAULT FRAME
        self.window.setWindowFlag(Qt.FramelessWindowHint)
        self.window.setAttribute(Qt.WA_TranslucentBackground)

        # SETTING SHADOW
        self.shadow = QGraphicsDropShadowEffect(self.window)
        self.shadow.setBlurRadius(20)
        self.shadow.setOffset(QPoint(0,0))
        self.shadow.setColor(QColor(0,0,0,100))

        self.secshadow = QGraphicsDropShadowEffect(self.window)
        self.secshadow.setBlurRadius(20)
        self.secshadow.setOffset(QPoint(0,0))
        self.secshadow.setColor(QColor(0,0,0,100))

        self.connect_ui.connect_qframe.setGraphicsEffect(self.shadow)
        self.chat_ui.chat_qframe.setGraphicsEffect(self.secshadow)

        # SETTING DRAG
        self.chat_ui.top_frame.mouseMoveEvent = self.window.move_window
        self.connect_ui.connect_qframe.mouseMoveEvent = self.window.move_window

        # SETTING MAX./RES. BUTTON
        self.chat_ui.window_button.clicked.connect(self.configure_maximized)
        # SETTING MIN. BUTTON
        self.chat_ui.minimize_button.clicked.connect(lambda: self.window.showMinimized())
        # SETTING CLOSE BUTTON
        self.chat_ui.exit_button.clicked.connect(self.closeapp)
        
        # SETTING SIZE GRIP
        self.sizegrip = QSizeGrip(self.chat_ui.grip_frame)
        self.sizegrip.setStyleSheet("QSizeGrip { background-color: none; width: 30px; height: 25px; }")

    def closeapp(self):
        self.window.recv_thread.terminate()
        self.window.tcp_client.close()
        self.window.close()

    def configure_maximized(self):

        if not self.window.isMaximized():
            self.window.showMaximized()
            self.chat_ui.chat_qwidget_vlayout.setContentsMargins(0,0,0,0)

        else:
            self.chat_ui.chat_qwidget_vlayout.setContentsMargins(10,10,10,10)
            self.window.showNormal()


