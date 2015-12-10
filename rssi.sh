#!/bin/sh -
export RSSI_CSV_FILE=$1
export DELAY=$2
while true
do
  iw dev wlp1s0 station dump | /home/root/439fa15/iwparser.py
  if [ -z "$DELAY" ]
    then
      sleep $DELAY
  fi
done
