#!/bin/sh
# This is just a wrapper that connects to the Galileo over USB for
# command execution.  You need to run the activate_cmd.ino sketch for this to
# work.

# Pass in the device mapped to the Galileo to this script.
# Ex: cmd.sh /dev/ttyACM0
screen $1 115200;
