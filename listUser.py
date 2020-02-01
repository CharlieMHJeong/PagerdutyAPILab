import requests

API_KEY = 'xja-DWfBeNv_zvuZuCdg'
QUERY = ''
TEAM_IDS = ['P7GN0I0']
INCLUDE = []

def list_users():
    url = 'https://api.pagerduty.com/users'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
    }
    payload = {
        'query': QUERY,
        'team_ids[]': TEAM_IDS,
        'include[]': INCLUDE
    }
    r = requests.get(url=url, headers=headers, params=payload)

    # r = requests.get(url=url, headers=headers)
    print('StatusCode: {code}'.format(code=r.status_code))
    print(r.json())

if __name__ == '__main__':
    list_users()