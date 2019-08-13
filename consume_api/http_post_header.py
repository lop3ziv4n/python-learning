import json

import requests

url = "http://httpbin.org/post"
data = {"nombre": "Ivan", "curso": "Python", "nivel": "Intermedio"}  # Dictionary
header = {"Content-Type": "application/json", "access-token": "aswqwft14ja"}  # Dictionary

response = requests.post(url, data=json.dumps(data), headers=header)

print(response.url)

if response.status_code == 200:
    print(response.content)
    response_header = response.headers  # Dictionary
    print(response_header)
    server = response_header["Server"]
    print(server)
