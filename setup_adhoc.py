#!/usr/bin/env python

import sys
import scriptline

def initialize(essid='hoc', interface='wlp1s0', ip='92.168.9.9/16', channel='4'):
    os.system('ip link set %s down' % interface)
    os.system('iwconfig %s mode ad-hoc' % interface)
    os.system('iwconfig %s channel %s' % (interface, channel))
    os.system("iwconfig %s essid '%s'" % (interface, essid))
    os.system('iwconfig %s key 1234567890' %interface)
    os.system('ip link set %s up' % interface)
    os.system('ip addr add %s dev %s', (sip, interface))
    os.system('iwconfig')

if __name__ == '__main__'
    scriptline.run()
