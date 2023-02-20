import socket
import sys

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5678

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv_sock.bind((SERVER_HOST, SERVER_PORT))
srv_sock.listen(50)

try:
    while True:
        client, address = srv_sock.accept()
        while True:
            data = client.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
            client.send(data + b' response')
except KeyboardInterrupt:
    srv_sock.close()
    print(end='\r')
    sys.exit()
