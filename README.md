# teamchecker
Python script which takes a Lichess team-id as input and outputs links to any engine users in the team.


## Usage

    ./teamchecker.py <teamId> [<teamId2> <teamId3>...]

    where <teamId> is the Team ID of the team you want to lookup the users for.
    You can find the Team ID from the URL in your Web Browser when you're browsing a team.
    It is the last part of the URL, https://lichess.org/team/<teamId>
    For example, the Team ID of the team Coders is "coders",
    as their team page is https://lichess.org/team/coders
