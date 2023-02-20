import os
import select
import socket
import sys
import time

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5678

# create a non-blocking socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setblocking(False)

# connect the client to the server
client_socket.connect_ex((SERVER_HOST, SERVER_PORT))

# set sys.stdin to non-blocking mode
sys.stdin = open(0)
old_stdin = sys.stdin
sys.stdin = os.fdopen(sys.stdin.fileno(), 'rb', buffering=0)

while True:
    # wait for input from either the socket or sys.stdin
    ready_to_read, ready_to_write, in_error = select.select(
        [client_socket, old_stdin], [client_socket], [client_socket], 0
    )

    # handle errors
    for s in in_error:
        print('Error with socket:', s)
        s.close()

    # read data from sys.stdin and send it to the server
    for sock in ready_to_write:
        if sock == client_socket:
            try:
                message = old_stdin.readline().strip()
                if message:
                    client_socket.send(message.encode())
            except BlockingIOError:
                pass

    # read data from the server and send it to stdout
    for sock in ready_to_read:
        if sock == client_socket:
            try:
                data = client_socket.recv(1024)
                if not data:
                    print('Connection closed by server.')
                    sys.exit()
                print(data.decode())
            except BlockingIOError:
                pass

    time.sleep(0.5)
