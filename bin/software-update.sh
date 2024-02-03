#!/bin/bash

git fetch
UPSTREAM=origin
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL != $REMOTE ]; then
    echo "Updating software from $LOCAL to $REMOTE"
    git reset --hard main
    git pull
    bin/post_software_update.sh
fi
