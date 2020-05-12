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


## Example of how to run the script from a Ubuntu/Debian computer

If you don't have **curl** (program to make HTTP requests) or **jq** installed,
you can install them with the package manager **apt** (or **apt-get**):

    user@ubuntu$ sudo apt install curl
    user@ubuntu$ sudo apt install jq

Then you can fetch the script with **curl**, and make it executable (**chmod**), and run it **./teamchecker.sh**:

    user@ubuntu$ curl -JO https://raw.githubusercontent.com/tors42/teamchecker/master/bash/teamchecker.sh
    user@ubuntu$ chmod +x teamchecker.sh
    user@ubuntu$ ./teamchecker.sh

## Example how to run the script in a fresh Ubuntu Docker container

    user@redhat$ docker run -it ubuntu

    root@ubuntu$ apt update && apt upgrade
    root@ubuntu$ apt install jq curl
    root$ubuntu$ curl -JO https://raw.githubusercontent.com/tors42/teamchecker/master/bash/teamchecker.sh
    root$ubuntu$ chmod +x teamchecker.sh
    root$ubuntu$ ./teamchecker.sh
