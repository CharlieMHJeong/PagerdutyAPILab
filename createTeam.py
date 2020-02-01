import pypd
import json

#PagerDuty Login details
PD_EMAIL = 'merong5780@naver.com'
API_KEY = 'xja-DWfBeNv_zvuZuCdg'

#TeamInfo
TeamName = 'Support_5'
TAGS = 'Support'
TeamData = {
    'name': TeamName,
    'tags': TAGS,
    }

def create_team():
    print("Team Creating:")
    print(json.dumps(TeamData, indent=2, sort_keys=True))

    r = pypd.Team.create(data=TeamData, api_key=API_KEY)
    print("Team Created!!\n")
    print(json.dumps(r.json, indent=2, sort_keys=True))

if __name__ == '__main__':
    create_team()
