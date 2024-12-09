import re
import requests
import mimetypes

# ip_html = requests.get('http://checkip.dyndns.org')
# ip_ = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ip_html.text)
# print(f'Seu ip é: {ip_[0]}')

m = mimetypes.guess_type('https://127.0.0.1:8000/test.html', strict=True)
print(m)