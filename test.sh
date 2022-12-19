#!/usr/bin/env bash

# cd notepad

git add .

DATE=$(date)

git commit -m "file added on $DATE"

git push

osascript -e "display notification 'pushed to git' with title 'SUCCESS'"