import pypd
import requests

#PagerDuty Login details
PD_EMAIL = 'merong5780@naver.com'
API_KEY = 'xja-DWfBeNv_zvuZuCdg'


TEAM_ID = 'PW2YG0T'
USER_ID = 'PK1F3K0'


def add_user_to_team():
    url = 'https://api.pagerduty.com/teams/{tid}/users/{uid}'.format(
        tid=TEAM_ID,
        uid=USER_ID
    )
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json'
    }
    r = requests.put(url=url, headers=headers)
    print('StatusCode: {code}'.format(code=r.status_code))
    print(r.text)


if __name__ == '__main__':
    add_user_to_team()



