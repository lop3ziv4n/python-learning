import requests

url = "https://i.imgur.com/bENDlkm.jpg"
response = requests.get(url, stream=True)  # stream = true, does not download content. keep connection

with open("image.jpg", "wb") as file:
    for chunk in response.iter_content():  # download content little by little
        file.write(chunk)

response.close()
