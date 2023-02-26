import socket
import threading

nickname = input('Choose a nickname:')

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5679

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect_ex((SERVER_HOST, SERVER_PORT))


def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'NICK':
                client_socket.send(nickname.encode())
            else:
                print(message)
        except:
            print('An error occured!')
            client_socket.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client_socket.send(message.encode())


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
