import json

import pypd

API_KEY = 'xja-DWfBeNv_zvuZuCdg'
PD_EMAIL = 'merong5780@naver.com'
ID = 'PE10DMU'

def delete_user():

    print("User To Delete: ")
    print(json.dumps(ID, indent=2, sort_keys=True))

    user = pypd.User.delete(ID, api_key=API_KEY)

    print("\nUser Deleted:")
    print(json.dumps(ID, indent=2, sort_keys=True))

if __name__ == '__main__':
    delete_user()