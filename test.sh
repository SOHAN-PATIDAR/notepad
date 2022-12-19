#!/usr/bin/env bash

# cd notepad

git add .

DATE=$(date)

git commit -m "file added on $DATE"

git push
