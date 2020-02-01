import pypd
import json

#PagerDuty Login details
PD_EMAIL = 'merong5780@naver.com'
API_KEY = 'xja-DWfBeNv_zvuZuCdg'

#New User Details
NAME = 'jeongm8'
EMAIL = 'jeongm8@hotmail.com'
ROLE = 'observer'

USER_DATA = {
    'type': 'user',
    'name': NAME,
    'email': EMAIL,
    'role': ROLE
}

def create_user():
    print("USER Creating: ")
    print(json.dumps(USER_DATA, indent=2, sort_keys=True))
    r = pypd.User.create(data=USER_DATA, api_key=API_KEY, from_email=PD_EMAIL)
    print("\nUser Created!!!")
    print(json.dumps(r.json, indent=2, sort_keys=True))


if __name__=='__main__':
    create_user()
