#Python 3.9.6
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
from random import randint
from sys import argv, exit
import socket, chatgui, connectgui

FORMAT = "utf-8"

class ReceiveThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, client_socket:socket.socket):
        super(ReceiveThread,self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_message()
    
    def receive_message(self):
        message = self.client_socket.recv(1024).decode(FORMAT)

        print(message)
        self.signal.emit(message)

class Client():
    def __init__(self):
        self.main_window = QMainWindow()
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connect_widget = QWidget(self.main_window)
        self.chat_widget = QWidget(self.main_window)

        self.chat_widget.setHidden(True)

        self.connect_ui = connectgui.Ui_connect_qwidget()
        self.connect_ui.setupUi(self.connect_widget)
        self.connect_ui.button_connect.clicked.connect(self.btn_connect_clicked)

        self.chat_ui = chatgui.Ui_chat_qwidget()
        self.chat_ui.setupUi(self.chat_widget)
        self.chat_ui.input_send_pbutton.clicked.connect(self.btn_send_clicked)

        self.main_window.resize(800,600)
        self.main_window.show()

    def btn_connect_clicked(self):
        ip = self.connect_ui.ip_ledit.text()
        port = self.connect_ui.port_ledit.text()
        nickname = self.connect_ui.nick_ledit.text()

        if len(ip) == 0:
            ip = "localhost"
        if len(port) == 0:
            port = 26000
        else:
            port = int(port)
        if len(nickname) == 0:
            nickname = "user_" + str(randint(1,1000))

        if self.connect(ip, port, nickname):
            self.connect_widget.setHidden(True)
            self.chat_widget.setVisible(True)

            self.recv_thread = ReceiveThread(self.tcp_client)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()

    def show_message(self, message:str):
        self.chat_ui.output_tbrowser.append(message)

    def connect(self, ip:str, port:int, nickname:str):
        try:
            self.tcp_client.connect((ip,port))
            self.tcp_client.send(nickname.encode(FORMAT))

            print("The client has successfuly connected to the server.")
            return True
        except Exception as err:
            print(err)
            return False

    def btn_send_clicked(self):
        text = self.chat_ui.input_tedit.toPlainText()
        self.tcp_client.send(text.encode(FORMAT))
        self.chat_ui.input_tedit.clear()

if __name__ == "__main__":
    app = QApplication(argv)
    clnt = Client()
    exit(app.exec())