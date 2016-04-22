#!/usr/bin/env bash
echo "To update Math Machine, you need to have git installed."
echo "Are you ready to update? [y,n]"
read confirm
if [ "$confirm" = "y" ]; then
  echo "Updating"
  git pull --rebase --stat origin master
    if [ $? -eq 0 ]; then
      echo "Math Machine has been updated!"
    else
      echo "Math Machine couldn't update. Try again later?"
    fi
else
  echo "Aborting"
  exit
fi
