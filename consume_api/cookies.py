import requests

url = "https://httpbin.org/cookies"
cookie = {"my-cookie": "true"}

response = requests.get(url, cookies=cookie)

if response.ok:
    cookies = response.cookies
    print(cookies)

    print("El contenido es: ")
    print(response.content)
