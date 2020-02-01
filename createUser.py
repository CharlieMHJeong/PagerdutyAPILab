import json
import requests

import pypd

API_KEY = 'xja-DWfBeNv_zvuZuCdg'
PD_EMAIL = 'merong5780@naver.com'
USER_DATA = {
    "type":"user",
    "name":"jeongm",
    "email":"jeongm@hotmail.com",
    "role":"team_responder",
    # "role":"rrr",
    # StatusCode: 400
    # {'error': {'message': 'Invalid Input Provided', 'code': 2001, 'errors': ['Role must be in read_only_user, read_only_limited_user, owner, admin, user, observer, limited_user, team_responder, or restricted_access.']}}

}

def create_user():
    url = 'https://api.pagerduty.com/users'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json',
        'From': PD_EMAIL
    }
    print("User to create: ")
    print(json.dumps(USER_DATA, indent=2, sort_keys=True))
    payload = {
        'user': USER_DATA,
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print('StatusCode: {code}'.format(code=r.status_code))
    print(r.json())

if __name__ == '__main__':
    create_user()




