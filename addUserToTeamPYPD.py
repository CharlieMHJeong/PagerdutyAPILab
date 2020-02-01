from os.path import dirname, join
from pprint import pprint, pformat


import pypd
import clean


result = None
all_run_lines = []


def run(s, exit_on_exception=True, pluck=None):
    all_run_lines.append(s)
    print('\n```\n>>> %s' % s)
    try:
        exec(s)
    except Exception as e:
        print('ERROR: %s' % e)
        if exit_on_exception:
            print('The demo is broken! So sad :(')
            exit()
    print('\n```\n')
    output = locals()

    if pluck is None:
        return output

    return locals().get(pluck)


def wait(s='Press enter to continue.\n'):
    try:
        return input(s)
    except KeyboardInterrupt:
        exit()
    except:
        pass



team_data = {
    'name': 'Presidents of the United States of America',
    'description': 'Only the best of the best. Only the Donalds.'
}

user_data = {
    'type': 'user',
    'name': 'Donald Drumpf',
    'color': 'green',
    'role': 'user',
    'job_title': 'Wall-Builder',
    'description': 'Making Python awesome again, one alert at a time!',
}

print('Make a team for the user\n===\n')
print('Now create a team for %s' % (user,))
team_data['name'] = wait('Enter team name: ') or team_data['name']
print('Creating team with details:\n')
print('team_data = \n%s' % (pformat(team_data)))
results = run('team = pypd.Team.create(data=team_data)')
team = results['team']
pprint(team.json)
print('\n\n')
wait()
# --- add the user to the team
print('Add the user to the team\n===\n')
print('Now add %s to %s' % (user, team))
results = run('team.add_user(user)')
wait()


