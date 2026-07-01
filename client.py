import socket
import threading

host, port = 'localhost', 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def handler(sock):
    buffersize = 1024

    while True:
        raw_data = sock.recv(buffersize)
        if raw_data == b'':
            break

        data = raw_data.decode('utf-8')
        print(data)

s.connect((host, port))

t = threading.Thread(target=handler, args=(s,), daemon=True)
t.start()

while True:
    message = input().encode('utf-8')

    if not message:
        continue

    s.sendall(message)
