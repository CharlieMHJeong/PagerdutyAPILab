import json

import pypd
from pypd.errors import BadRequest

API_KEY = 'xja-DWfBeNv_zvuZuCdg'
PD_EMAIL = 'merong5780@naver.com'
USER_DATA = {
    "type":"user",
    "name":"jeongm3",
    "email":"jeongm3@hotmail.com",
    # "role":"rrr",
    "role":"team_responder",
}

def create_user():
    try:
        print("User to create: ")
        print(json.dumps(USER_DATA, indent=2, sort_keys=True))
        response = pypd.User.create(data=USER_DATA, from_email=PD_EMAIL, api_key=API_KEY)
        print("\nUser Created:")
        print(json.dumps(response.json, indent=2, sort_keys=True))

    except BadRequest as ex:
        msg = "\nPagerDuty API Call failed \nCode: {code} \nMessage: {message} \n{errors} ".format(code=ex.code, message=ex.message, errors=ex.errors )
        print(msg)

if __name__ == '__main__':
    create_user()