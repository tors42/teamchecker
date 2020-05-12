# teamchecker

Python script which takes a Lichess team-id as input and outputs links to any engine users in the team.

## Usage

    ./teamchecker.py <teamId> [<teamId2> <teamId3>...]

    where <teamId> is the Team ID of the team you want to lookup the users for.
    You can find the Team ID from the URL in your Web Browser when you're browsing a team.
    It is the last part of the URL, https://lichess.org/team/<teamId>
    For example, the Team ID of the team Coders is "coders",
    as their team page is https://lichess.org/team/coders

## Dependencies

    - Python 3
    - Python modules "ndjson" and "requests"

    Quick instructions:
    # apt install python3
    # apt install python3-pip
    # pip3 install ndjson
    # pip3 install requests

## Example how to run the script in a fresh Ubuntu Docker container

    user@localhost$ docker run -it ubuntu

    root@container$ apt update && apt upgrade
    root$container$ apt install python3 python3-pip
    root$container$ pip3 install ndjson requests
    root@container$ apt install curl
    root$container$ curl -JO https://raw.githubusercontent.com/tors42/teamchecker/master/python/teamchecker.py
    root$container$ chmod +x teamchecker.py
    root$container$ ./teamchecker.py
