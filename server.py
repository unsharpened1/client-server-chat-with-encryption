import socket
import threading

host, port = 'localhost', 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

clients = []
clients_lock = threading.Lock()

def handler(sock):
	buffersize = 1024

	while True:
		raw_data = sock.recv(buffersize)

		if raw_data == b'':
			with clients_lock:
				for i in range(len(clients)):
					if clients[i] == sock:
						clients.pop(i)

			sock.close()
			return
			
		with clients_lock:
			for i in clients:
				if i != sock:
					i.sendall(raw_data)
				else:
					continue

s.listen()

while True:
	client_socket, client_address = s.accept()

	with clients_lock:
		clients.append(client_socket)

	t = threading.Thread(target=handler, args=(client_socket,))
	t.start()