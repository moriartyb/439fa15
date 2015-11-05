#!/usr/bin/env python

import sys
import os

def initialize_adhoc(**kwargs):
    interface = kwargs['interface'] if 'interface' in kwargs else 'wlp1s0'
    channel = kwargs['channel'] if 'channel' in kwargs else '4'
    essid = kwargs['essid'] if 'essid' in kwargs else 'hoc'
    ip = kwargs['ip'] if 'ip' in kwargs else '192.168.9.9/16'

    os.system('ip link set %s down' % interface)
    os.system('iwconfig %s mode ad-hoc' % interface)
    os.system('iwconfig %s channel %s' % (interface, channel))
    os.system("iwconfig %s essid '%s'" % (interface, essid))
    os.system('iwconfig %s key 1234567890' % interface)
    os.system('ip link set %s up' % interface)
    os.system('ip addr flush dev %s' % interface)
    os.system('ip addr add %s dev %s' % (ip, interface))
    print 'done!'

if __name__ == '__main__':
    arguments = sys.argv[1:]
    keys = arguments[::2]
    values = arguments[1::2]
    kwargs = {}
    for i in range(0, len(keys)):
        kwargs[keys[i]] = values[i]

    initialize_adhoc(**kwargs)
