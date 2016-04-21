#!/usr/bin/env bash
echo "To update Math Machine, you need to have git installed."
echo "Are you ready to update? [y,n]"
read confirm
if [ "$confirm" = "y" ]; then
  echo "Updating"
  git pull --rebase --stat origin master
    echo "Math Machine has been updated."
    exit
else
  echo "Aborting"
  exit
fi
