import requests
import json

#PagerDuty Login details
PD_EMAIL = 'merong5780@naver.com'
API_KEY = 'xja-DWfBeNv_zvuZuCdg'

#New User Details
NAME = 'jeongm4'
EMAIL = 'jeongm4@hotmail.com'
ROLE = 'user'


def create_user():
    url = 'https://api.pagerduty.com/users'
    headers = {
        'Accept':'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json',
        'From': PD_EMAIL,
    }
    payload={
        'user': {
            'type': 'user',
            'name': NAME,
            'email': EMAIL,
            'role': ROLE
        }
    }
    r = requests.post(url=url, headers=headers, data=json.dumps(payload))
    print('StatusCode: {code}'.format(code=r.status_code))
    print(r.json())

if __name__=='__main__':
    create_user()



