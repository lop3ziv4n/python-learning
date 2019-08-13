# https://developer.github.com/v3/repos/#get

import requests

access_token = "373000f72e50c19b24a930893e1b4ef322b85802"

url = "https://api.github.com/user/repos"
header = {"Authorization": "token 373000f72e50c19b24a930893e1b4ef322b85802"}

response = requests.get(url, headers=header)

print(response.url)

if response.status_code == 200:
    content = response.content
    print(content)

    payload = response.json()
    for project in payload:
        name = project("name")
        print(name)
else:
    print(response.content)
