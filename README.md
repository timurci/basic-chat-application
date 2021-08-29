# basic-chat-application
# by timurci

DESCRIPTION
======================

This chat application has been developed for practicing socket and PyQT5 modules in Python, also creating an appealing GUI instead of dull default interface. The server can be run locally, therefore providing a private communication.

The application has been developed using:
    - Python 3.9.6
    - PyQT5 5.15.2

USING APPLICATION
======================
Host should run, "server.py":

    The server runs on TCP and the clients should connect by using ipv4 address of the host.
    There is no check for closing the server, the process must be terminated either by closing the console or killing the process.
    Connections, disconnections and messages are displayed on console.

    If no ip and/or port is set while starting the server, the default will be set:
    => ip: "localhost", port: 26000

    Please make sure your firewall does not prevent others from connecting to your server.
    Other clients can connect if you have an open port or a virtual network such as provided by LogMeIn Hamachi.

User should run, "client.py":

    The user should connect with ipv4 address of the host.
    Connection defaults are displayed on empty input of the connection interface, 
    the default settings will be used in case the information would not be provided.
