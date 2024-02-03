#!/bin/bash

MINUTES=5
sleep $((MINUTES * 60))
git fetch
UPSTREAM=origin
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL != $REMOTE ]; then
    echo "Updating software from $LOCAL to $REMOTE"
    git reset --hard master
    git pull
    sudo systemctl restart photo-screen
fi
