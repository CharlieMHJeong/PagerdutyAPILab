import requests
import json

import pypd

API_KEY = 'xja-DWfBeNv_zvuZuCdg'
PD_EMAIL = 'merong5780@naver.com'
ID = 'PE10DMU'

def delete_user():
    url = 'https://api.pagerduty.com/users/{id}'.format(id=ID)
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
    }

    r = requests.delete(url=url, headers=headers)
    print('StatusCode: {code}'.format(code=r.status_code))
    print(r.text)

if __name__ == '__main__':
    delete_user()