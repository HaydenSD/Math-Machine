#!/usr/bin/env bash
echo "To update Math Machine, you need to have git installed."
echo "Are you ready to update? [y,n]"
read confirm
if [ "$confirm" = "y" ]; then
  echo "Updating"
  git pull --rebase --stat origin master
    if [ $? -eq 0 ]; then
      echo "Math Machine has been updated!"
      printf '_____          __  .__         _____                .__    .__                  '
      printf '/     \ _____ _/  |_|  |__     /     \ _____    ____ |  |__ |__| ____   ____    '
      printf '/  \ /  \\__  \\   __\  |  \   /  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \  '
      printf '/    Y    \/ __ \|  | |   Y  \ /    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/ '
      printf '\____|__  (____  /__| |___|  / \____|__  (____  /\___  >___|  /__|___|  /\___  >'
      printf '\/     \/          \/          \/     \/     \/     \/        \/     \/         '
    else
      echo "Math Machine couldn't update. Try again later?"
    fi
else
  echo "Aborting"
  exit
fi
