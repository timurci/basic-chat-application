import socket, threading

FORMAT = "utf-8"

class Server():
    def __init__(self,host:str,port:int):
        self.clients = {}

        self.tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server.bind((host,port))
        self.tcp_server.listen()

        print("[THE SERVER IS RUNNING]")

        while True:
            conn, addr = self.tcp_server.accept()

            nickname = conn.recv(1024).decode(FORMAT)
            self.clients[nickname] = conn

            threading.Thread(target=self.receive_message, args=(conn, nickname), daemon=True).start()
            print("New connection from \t{}\t{}".format(addr,nickname))

    def receive_message(self, connection:socket.socket, nickname:str):
        while True:
            try:
                message_en = connection.recv(1024)
                self.send_message(message_en, nickname)
                print(nickname + ": " + message_en.decode(FORMAT))

            except socket.error:
                print("Client " + nickname + " has been disconnected.")
                connection.close()
                del(self.clients[nickname])
                break
            except Exception as err:
                print(err)
                connection.close()
                del(self.clients[nickname])
                break

    def send_message(self, message:str, sender:str):
        if len(self.clients) > 0:
            message = message.decode(FORMAT).replace("\n","<br>")
            msg = "<p style=\"font: 15px Calibri Light;\">" + "<span style=\"font-weight: bold;\">" + sender + ":</span><br>" + message + "</p>"
            msg = msg.encode(FORMAT)
            for nickname in self.clients:
                self.clients[nickname].send(msg)

if __name__ == "__main__":
    host = input("IP:\t")
    port = input("PORT:\t")
    if len(host.strip()) == 0:
        host = "localhost"
    if len(port.strip()) == 0:
        port = 26000
    else:
        port = int(port)
    print("---\nSET\n---")
    print("IP\t"+ host)
    print("PORT\t" + str(port))
    Server(host,port)