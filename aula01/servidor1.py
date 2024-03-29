import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

client_connection, client_address = server_socket.accept()

request = client_connection.recv(1024).decode()

print(request)

response = 'HTTP/1.1 200 OK\n\nHello World'
client_connection.sendall(response.encode())
# print('Um cliente se conectou!')

client_connection.close()
server_socket.close()
