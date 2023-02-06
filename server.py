import socket
import threading
import datetime

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
DATE = datetime.datetime.today()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

def handle_client(conn, addr):
    print(f'[New CONNECTION] {addr} connected' )

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length =int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr}] {msg}')

    conn.close()


def start_server():
    server.listen()
    print(f'[Sent Date : {DATE}] Server is listening on {SERVER} ')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')


start_server()