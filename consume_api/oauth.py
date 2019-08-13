# https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/
# https://developer.github.com/v3/oauth_authorizations/
# https://github.com/settings/developers
import requests

client_id = "369215fa00432fdc6b039"
client_secret = "bcce45a5a7943981210e8f7cb1425bf1541507a"

# https://github.com/login/oauth/authorize?client_id=369215fa00432fdc6b039&scope=repo
code = "35d1a2ef36db2d2dbc24"

url = "https://github.com/login/oauth/access_token"
payload = {"client_id": client_id, "client_secret": client_secret, "code": code}
header = {"Accept": "application/json"}

response = requests.post(url, json=payload, headers=header)

print(response.url)

if response.status_code == 200:
    content = response.content
    print(content)

    response_json = response.json()
    access_token = response_json("access_token")
    print(access_token)
