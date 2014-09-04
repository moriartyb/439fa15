#!/bin/bash

# steps:
#   1. change the first line below to have a unique IP
#   2. copy this script into /etc/init.d/
#   3. edit its permissions while in /etc/init.d/ with: 
#     chmod +x startup.sh
#   4. create the symlink with:
#     update-rc.d startup.sh defaults
#   5. profit

python /home/root/439fa15/setup_adhoc.py ip 192.168.3.3/24 # modify this on each galileo to be unique.
