# teamchecker.sh

Bash script which takes a Lichess team-id as input and outputs links to any engine users in the team.

## Usage

    ./teamchecker.sh [teamId]

    where [teamId] is the Team ID of the team you want to lookup the users for.
    You can find the Team ID from the URL in your Web Browser when you're browsing a team.
    It is the last part of the URL, https://lichess.org/team/<teamId>
    For example, the Team ID of the team Coders is "coders",
    as their team page is https://lichess.org/team/coders

## Dependencies

    - curl ( https://curl.haxx.se/ )
    - jq   ( https://stedolan.github.io/jq/ )

    Quick instructions:

    apt install curl
    apt install jq

## Example how to run the script in a fresh Ubuntu Docker container

    user@localhost$ docker run -it ubuntu

    root@container$ apt update && apt upgrade
    root@container$ apt install jq curl
    root$container$ curl -JO https://raw.githubusercontent.com/tors42/teamchecker/master/bash/teamchecker.sh
    root$container$ chmod +x teamchecker.sh
    root$container$ ./teamchecker.sh