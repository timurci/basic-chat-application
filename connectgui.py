# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\connectwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_connect_qwidget(object):
    def setupUi(self, connect_qwidget):
        connect_qwidget.setObjectName("connect_qwidget")
        connect_qwidget.resize(800, 600)
        connect_qwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.connect_qwidget_vlayout = QtWidgets.QVBoxLayout(connect_qwidget)
        self.connect_qwidget_vlayout.setContentsMargins(10, 10, 10, 10)
        self.connect_qwidget_vlayout.setSpacing(0)
        self.connect_qwidget_vlayout.setObjectName("connect_qwidget_vlayout")
        self.connect_qframe = QtWidgets.QFrame(connect_qwidget)
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.connect_qframe.setFont(font)
        self.connect_qframe.setStyleSheet("border:none;\n"
"border-radius: 11px;\n"
"background-color: qlineargradient(spread:pad, x1:0.124, y1:0.0454545, x2:0.711403, y2:0.46, stop:0 rgba(104, 100, 141, 255), stop:0.870647 rgba(57, 55, 77, 255));")
        self.connect_qframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.connect_qframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.connect_qframe.setObjectName("connect_qframe")
        self.connect_qframe_glayout = QtWidgets.QGridLayout(self.connect_qframe)
        self.connect_qframe_glayout.setContentsMargins(0, 0, 0, 0)
        self.connect_qframe_glayout.setSpacing(0)
        self.connect_qframe_glayout.setObjectName("connect_qframe_glayout")
        spacerItem = QtWidgets.QSpacerItem(137, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.connect_qframe_glayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.connect_qframe_glayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(137, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.connect_qframe_glayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.connect_qframe_glayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.connect_content_frame = QtWidgets.QFrame(self.connect_qframe)
        self.connect_content_frame.setMinimumSize(QtCore.QSize(500, 400))
        self.connect_content_frame.setMaximumSize(QtCore.QSize(500, 400))
        self.connect_content_frame.setStyleSheet("background-color: rgba(215, 236, 255, 80);\n"
"border: none;")
        self.connect_content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.connect_content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.connect_content_frame.setObjectName("connect_content_frame")
        self.connect_content_layout = QtWidgets.QVBoxLayout(self.connect_content_frame)
        self.connect_content_layout.setContentsMargins(0, 0, 0, 0)
        self.connect_content_layout.setSpacing(0)
        self.connect_content_layout.setObjectName("connect_content_layout")
        self.nick_frame = QtWidgets.QFrame(self.connect_content_frame)
        self.nick_frame.setStyleSheet("background-color: none;")
        self.nick_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nick_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nick_frame.setObjectName("nick_frame")
        self.nick_layout = QtWidgets.QHBoxLayout(self.nick_frame)
        self.nick_layout.setContentsMargins(10, 10, 12, 10)
        self.nick_layout.setObjectName("nick_layout")
        self.nick_label = QtWidgets.QLabel(self.nick_frame)
        self.nick_label.setMinimumSize(QtCore.QSize(100, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nick_label.setFont(font)
        self.nick_label.setStyleSheet("color: black;\n"
"background-color: none;")
        self.nick_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nick_label.setObjectName("nick_label")
        self.nick_layout.addWidget(self.nick_label)
        self.nick_ledit = QtWidgets.QLineEdit(self.nick_frame)
        self.nick_ledit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(11)
        self.nick_ledit.setFont(font)
        self.nick_ledit.setStyleSheet("color: black;\n"
"background-color: rgba(255, 255, 255, 100);")
        self.nick_ledit.setObjectName("nick_ledit")
        self.nick_layout.addWidget(self.nick_ledit)
        self.connect_content_layout.addWidget(self.nick_frame)
        self.ip_frame = QtWidgets.QFrame(self.connect_content_frame)
        self.ip_frame.setStyleSheet("background-color: none;")
        self.ip_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ip_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ip_frame.setObjectName("ip_frame")
        self.ip_layout = QtWidgets.QHBoxLayout(self.ip_frame)
        self.ip_layout.setContentsMargins(10, 10, 12, 10)
        self.ip_layout.setObjectName("ip_layout")
        self.ip_label = QtWidgets.QLabel(self.ip_frame)
        self.ip_label.setMinimumSize(QtCore.QSize(100, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ip_label.setFont(font)
        self.ip_label.setStyleSheet("color: black;\n"
"background-color: none;")
        self.ip_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ip_label.setObjectName("ip_label")
        self.ip_layout.addWidget(self.ip_label)
        self.ip_ledit = QtWidgets.QLineEdit(self.ip_frame)
        self.ip_ledit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(11)
        self.ip_ledit.setFont(font)
        self.ip_ledit.setStyleSheet("color: black;\n"
"background-color: rgba(255, 255, 255, 100);")
        self.ip_ledit.setObjectName("ip_ledit")
        self.ip_layout.addWidget(self.ip_ledit)
        self.connect_content_layout.addWidget(self.ip_frame)
        self.port_frame = QtWidgets.QFrame(self.connect_content_frame)
        self.port_frame.setStyleSheet("background-color: none;")
        self.port_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.port_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.port_frame.setObjectName("port_frame")
        self.port_layout = QtWidgets.QHBoxLayout(self.port_frame)
        self.port_layout.setContentsMargins(10, 10, 12, 10)
        self.port_layout.setObjectName("port_layout")
        self.port_label = QtWidgets.QLabel(self.port_frame)
        self.port_label.setMinimumSize(QtCore.QSize(100, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.port_label.setFont(font)
        self.port_label.setStyleSheet("color: black;\n"
"background-color: none;")
        self.port_label.setAlignment(QtCore.Qt.AlignCenter)
        self.port_label.setObjectName("port_label")
        self.port_layout.addWidget(self.port_label)
        self.port_ledit = QtWidgets.QLineEdit(self.port_frame)
        self.port_ledit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(11)
        self.port_ledit.setFont(font)
        self.port_ledit.setStyleSheet("color: black;\n"
"background-color: rgba(255, 255, 255, 100);")
        self.port_ledit.setObjectName("port_ledit")
        self.port_layout.addWidget(self.port_ledit)
        self.connect_content_layout.addWidget(self.port_frame)
        self.button_frame = QtWidgets.QFrame(self.connect_content_frame)
        self.button_frame.setMinimumSize(QtCore.QSize(0, 90))
        self.button_frame.setMaximumSize(QtCore.QSize(16777215, 90))
        self.button_frame.setStyleSheet("background-color: none;")
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.button_layout = QtWidgets.QVBoxLayout(self.button_frame)
        self.button_layout.setContentsMargins(0, 0, 0, 25)
        self.button_layout.setObjectName("button_layout")
        self.button_warning_label = QtWidgets.QLabel(self.button_frame)
        self.button_warning_label.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(8)
        self.button_warning_label.setFont(font)
        self.button_warning_label.setStyleSheet("color: rgb(181, 85, 147);\n"
"color: rgb(84, 26, 51);")
        self.button_warning_label.setText("")
        self.button_warning_label.setAlignment(QtCore.Qt.AlignCenter)
        self.button_warning_label.setObjectName("button_warning_label")
        self.button_layout.addWidget(self.button_warning_label)
        self.button_connect = QtWidgets.QPushButton(self.button_frame)
        self.button_connect.setMinimumSize(QtCore.QSize(80, 35))
        self.button_connect.setMaximumSize(QtCore.QSize(80, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_connect.setFont(font)
        self.button_connect.setStyleSheet("QPushButton{\n"
"color: white;\n"
"background-color: rgb(153, 186, 208,150);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(199, 243, 255);\n"
"    background-color: rgb(126, 146, 166,150);\n"
"}\n"
"")
        self.button_connect.setObjectName("button_connect")
        self.button_layout.addWidget(self.button_connect, 0, QtCore.Qt.AlignHCenter)
        self.connect_content_layout.addWidget(self.button_frame)
        self.connect_qframe_glayout.addWidget(self.connect_content_frame, 1, 1, 1, 1)
        self.connect_qwidget_vlayout.addWidget(self.connect_qframe)

        self.retranslateUi(connect_qwidget)
        QtCore.QMetaObject.connectSlotsByName(connect_qwidget)

    def retranslateUi(self, connect_qwidget):
        _translate = QtCore.QCoreApplication.translate
        connect_qwidget.setWindowTitle(_translate("connect_qwidget", "Form"))
        self.nick_label.setText(_translate("connect_qwidget", "Nickname"))
        self.nick_ledit.setPlaceholderText(_translate("connect_qwidget", "user_xxxx"))
        self.ip_label.setText(_translate("connect_qwidget", "IP Address"))
        self.ip_ledit.setPlaceholderText(_translate("connect_qwidget", "localhost"))
        self.port_label.setText(_translate("connect_qwidget", "Port"))
        self.port_ledit.setPlaceholderText(_translate("connect_qwidget", "26000"))
        self.button_connect.setText(_translate("connect_qwidget", "Connect"))
