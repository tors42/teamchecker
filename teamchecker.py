#!/usr/bin/env python3

import ndjson
import requests
import sys
import time

def readTeamIds():

    if len(sys.argv) == 1:
        print('')
        print('Usage:')
        print(' ', sys.argv[0], '<teamId> [<teamId2> <teamId3>...]')
        print('')
        print('where <teamId> is the Team ID of the team you want to lookup the users for.')
        print('You can find the Team ID from the URL in your Web Browser when you\'re browsing a team.')
        print('It is the last part of the URL, https://lichess.org/team/<teamId>')
        print('For example, the Team ID of the team Coders is "coders",')
        print('as their team page is https://lichess.org/team/coders')
        print('')
        teamIdsString = input('Enter Team ID/s: ')
        teamIds = teamIdsString.split(' ')
    else:
        teamIds = sys.argv[1:]

    if not teamIds:
        print('No Team ID/s specified, exiting')
        sys.exit()

    return teamIds


def lookupUsersForTeamId( teamId ):
    url = 'https://lichess.org/api/team/' + teamId + '/users'
    print('Looking up users from ', url)
    start = time.time()
    response = requests.get(url=url)
    print('HTTP Request took ', time.time() - start, ' seconds')
    users = None
    if response.status_code == 200:
        #start = time.time()
        users = ndjson.loads(response.text)
        #stop = time.time()
        #print('Parsing response took ', stop - start, ' seconds')
    elif response.status_code == 429:
        print('Lichess API is under stress - retrying in a minute')
        time.sleep(60)
        response = requests.get(url=url)
        if response.status_code == 200:
            users = ndjson.loads(response.text)
        elif response.status_code == 429:
            print('Lichess API is still under stress - aborting')
            sys.exit()
        else:
            print('Failed retry of lookup ' + url + ' - HTTP status code', response.status_code)
    else:
        print('Failed to lookup ' + url + ' - HTTP status code', response.status_code)

    return users;


##
# For "offline" testing
# Provide the path to the file downloaded from 'https://lichess.org/api/team/<team-id>/users'
##
def lookupUsersFromFile( inputfile ):
    print('Looking up users from ', inputfile)
    with open(inputfile) as f:
        users = ndjson.load(f)
        return users
    return None


teamIds = readTeamIds()

for teamId in teamIds:

    users = lookupUsersForTeamId(teamId)

    #For "offline" testing
    #users = lookupUsersFromFile('/path/to/file/containing/users')

    if users:
        engine_users = []
        for user in users:
            if 'engine' in user:
                if user['engine']:
                    engine_users.append(user['url'])

        if len(engine_users) > 0:
            print('Team ' + teamId + ' has', len(engine_users), 'engine user/s (out of', len(users), 'members.)')
            print('')
            print(engine_users)
        else:
            print('No engine users found in ' + teamId + ' (out of', len(users), 'members.)')

    print()
    time.sleep(1)
