#/bin/bash

echo "In order to update Math Machine, you must have git installed."
echo "Are you ready to install updates? [y,n]"
read confirm
if [ "$confirm" = "y" ] || if [ "$confirm" = "Y" ]; then
  echo "Updating"
  if git pull --rebase --stat origin master
  then
    echo "Math Machine has been updated!"
  else
    echo "Math Machine could not update. Please try again later."
    exit
  fi
else
  echo "Aborting"
  exit
fi
