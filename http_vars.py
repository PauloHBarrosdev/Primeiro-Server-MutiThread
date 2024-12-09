def montar_retorno_http(arquivo_nome, arq_type):

    cabecalhos_http_response = [
                'HTTP/1.1 200 OK',
                f'Content-Type: {arq_type}'
            ]
    
    
    if arq_type in ('text/html', 'text/css', 'application/javascript',\
                     'application/x-python-code'):
        with open(arquivo_nome, 'r') as arq:
            conteudo = arq.read()
        cabecalhos_http_response.append(f'Content-Lenght: {len(conteudo)}')
        cabecalho_retorno = '\n'.join(cabecalhos_http_response)
        resposta = '\r\n\r\n'.join((cabecalho_retorno, conteudo))
        return resposta.encode()
    
    elif arq_type == 'image/x-icon':
        with open(arquivo_nome, 'rb') as arq:
            conteudo = arq.read()
        cabecalhos_http_response.append(f'Content-Lenght: {len(conteudo)}')
        cabecalho_retorno = '\n'.join(cabecalhos_http_response)
        cabecalho_retorno_encode = (cabecalho_retorno + '\r\n\r\n').encode()
        cabecalho_retorno_encode += conteudo
        return cabecalho_retorno_encode

class Parser_http:
    def __init__(self, request):
        self.request_lines = request.decode().split('\n')
        self.metodo = (self.request_lines[0].split(' '))[0]
        self.recurso = (self.request_lines[0].split(' '))[1]




if __name__ == '__main__':
    print(montar_retorno_http('teste.html', 'html/text'))