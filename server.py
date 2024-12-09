import socket
import http_vars
from threading import Thread

class Server:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 8000    
        return None

    def vincular_endereco(self, endereco, backlog):
        self.server_socket.bind((endereco, self.port))
        self.server_socket.listen(backlog)
        return None

    def congelar_para_conexão(self):
        client_socket, client_address = self.server_socket.accept()
        return client_socket, client_address

class ConectionSocket:
    def __init__(self, client_socket, client_address):
        self.client_socket = client_socket
        self.client_address = client_address
        self.client_request: http_vars.Parser_http = http_vars.Parser_http(self.client_socket.recv(3000))


def process_request(conexao):
    
        print(conexao.client_request.recurso)
        resposta = recursos.get(conexao.client_request.recurso)
        if not resposta:
            conexao.client_socket.sendall(http_vars.montar_retorno_http('404.html', 'text/html'))
            conexao.client_socket.close()
            
        else:
            conexao.client_socket.sendall(resposta)
            conexao.client_socket.close()
        return conexao

try:
    if __name__ == '__main__':
        servidor = Server()
        servidor.port = 8000
        servidor.vincular_endereco('127.0.0.1', 10)
        recursos = {
            '/': http_vars.montar_retorno_http('teste.html', 'text/html'),
            '/favicon.png': http_vars.montar_retorno_http('favicon.png', 'image/x-icon'),
            '/site.css': http_vars.montar_retorno_http('site.css', "text/css"),
            '/site.js': http_vars.montar_retorno_http\
                ('site.js', 'application/javascript'),
            '/script.py': http_vars.montar_retorno_http('script.py', 'application/x-python-code')
        }
        print(f'SERVER LOCAL - PORTA {servidor.port}')
        while True:
            conexao = ConectionSocket(*servidor.congelar_para_conexão())
            thread = Thread(target=process_request, \
                   args=(conexao, ))
            thread.start()
            
except KeyboardInterrupt:
    conexao.client_socket.close()
    servidor.server_socket.close()