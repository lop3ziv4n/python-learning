import json

import requests

url = "http://httpbin.org/get"
args = {"nombre": "Ivan", "curso": "Python", "nivel": "Intermedio"}
response = requests.get(url, params=args)

print(response.url)

if response.status_code == 200:
    """ 
    response_json = response.json()  # Dictionary
    origin = response_json['origin']
    print(origin)
    
    """

    response_json = json.loads(response.text)
    origin = response_json['origin']
    print(origin)
