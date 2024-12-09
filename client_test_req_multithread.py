from threading import Thread
import requests

def request_page(req_n):
    print(f'Requesting page {req_n}')
    req = requests.get('http://localhost:8000/')
    print(f'Requisição {req_n} finalizada')

threads =[]
if __name__ == '__main__':
    for v in range(4):
        threads.append(Thread(target=request_page, args=(v, )))
        threads[v].start()

