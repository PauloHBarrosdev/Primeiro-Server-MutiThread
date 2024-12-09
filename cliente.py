import socket
from server import PORTA_SERVER, IP_SERVER

#crio um objeto socket para o cliente
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# crio a conexão
socket_cliente.connect((IP_SERVER, PORTA_SERVER))
mensagem = 'Mensagem enviada'

print(f'Vou mandar a mensagem "{mensagem}"')

mensagem = mensagem.encode()
socket_cliente.sendall(mensagem)

# aguarda uma resposta, quando chegar, retorna a resposta
resposta = socket_cliente.recv(1024)

print(f'O servidor respondeu "{resposta.decode()}"')

# retorno = socket_cliente.recv(1024)
# print(retorno)
socket_cliente.close()