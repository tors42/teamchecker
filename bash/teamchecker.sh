#!/bin/bash

hash curl
hash jq

if [ $# -eq 0 ]; then
    echo
    echo "Usage:"
    echo
    echo "  $0 <teamId>"
    echo
    echo "where <teamId> is the Team ID of the team you want to lookup the users for."
    echo "You can find the Team ID from the URL in your Web Browser when you're browsing a team."
    echo "It is the last part of the URL, https://lichess.org/team/<teamId>"
    echo "For example, the Team ID of the team Coders is \"coders\","
    echo "as their team page is https://lichess.org/team/coders"
    echo ""
    echo "Enter Team ID: "
    read TEAMID
else
    TEAMID=$1
fi

TMPFILE=$(mktemp)
echo "Looking up users for team ${TEAMID}"
curl -o ${TMPFILE} https://lichess.org/api/team/${TEAMID}/users
echo ""
[[ $? -ne 0 ]] && echo "Failed to lookup team members for team ${TEAMID}" && rm ${TMPFILE} && exit

NUMUSERS=$(cat ${TMPFILE} | wc -l)

[[ $NUMUSERS -eq 0 ]] && echo "Didn't find any team members for team ${TEAMID}" && rm ${TMPFILE} && exit

TOSVUSERS=$(cat ${TMPFILE} | jq --raw-output 'select(.tosViolation == true ) | .url')
rm ${TMPFILE}

if [ -z "${TOSVUSERS}" ]; then
    echo "No found ToS warned users in team ${TEAMID} (of ${NUMUSERS} members)"
else
    NUMTOSVUSERS=$(echo "${TOSVUSERS}" | wc -l)
    echo "Found ${NUMTOSVUSERS} ToS warned users found in team ${TEAMID} (of ${NUMUSERS} members)"
    echo "${TOSVUSERS}"
fi
