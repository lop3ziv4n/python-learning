import requests

access_token = "373000f72e50c19b24a930893e1b4ef322b85802"

url = "https://api.github.com/user/repos"
payload = {"name": "git_api_test"}
header = {"Accept": "application/json", "Authorization": "token" + access_token}

response = requests.post(url, json=payload, headers=header)

print(response.url)

if response.status_code == 200:
    print(response.json())
else:
    print(response.content)
