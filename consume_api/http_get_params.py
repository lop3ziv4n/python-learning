# http://httpbin.org page http request & response service

import requests

url = "http://httpbin.org/get"
args = {"nombre": "Ivan", "curso": "Python", "nivel": "Intermedio"}
response = requests.get(url, params=args)

print(response.url)

if response.status_code == 200:
    content = response.content
    print(content)
