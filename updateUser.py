import requests
import json

API_KEY = 'xja-DWfBeNv_zvuZuCdg'
ID = 'PHR2CNR'
QUERY = ''
USER_DATA = {
    "name":"jeongm",
    "email":"jeongm2@hotmail.com",
    # "role":"rrr",
    "role":"team_responder",
}

def update_user():
    url = 'https://api.pagerduty.com/users/{id}'.format(id=ID)
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json',
    }
    payload = {'user':USER_DATA }
    r = requests.put(url=url, headers=headers, data=json.dumps(payload))
    print('StatusCode: {code}'.format(code=r.status_code))
    print(r.json())

if __name__ == '__main__':
    update_user()