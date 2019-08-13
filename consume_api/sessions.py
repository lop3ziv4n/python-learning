import requests

session = requests.session()
session.auth = ("user", "pass")

url = "https://api.github.com/user"
response = session.get(url)
if response.ok:
    print(response.content)

url = "https://github.com/ilopez"
response = session.get(url)
if response.ok:
    print(response.content)
    print(response.cookies)
