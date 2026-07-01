import socket
import threading

host, port = 'localhost', 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

clients = []

def handler(sock):
	buffersize = 1024

	while True:
		raw_data = sock.recv(buffersize)
		if raw_data == b'':
			sock.close()
			return

		for i in clients:
			if i != sock:
				i.sendall(raw_data)
			else:
				continue

s.listen()

while True:
	client_socket, client_address = s.accept()
	clients.append(client_socket)

	t = threading.Thread(target=handler, args=(client_socket,))
	t.start()