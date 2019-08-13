import json

import requests

url = "http://httpbin.org/post"
data = {"nombre": "Ivan", "curso": "Python", "nivel": "Intermedio"}  # Dictionary
# response = requests.post(url, json=data)  # internal serialization post
response = requests.post(url, data=json.dumps(data))  # external serialization post

print(response.url)

if response.status_code == 200:
    print(response.content)
