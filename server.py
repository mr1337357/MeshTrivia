import sys
import time
import argparse
from pubsub import pub

import meshtastic
import meshtastic.tcp_interface
import meshtastic.serial_interface

from ini import ini

interface = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='MeshTrivia', description='Trivia over MeshTastic')
    parser.add_argument('-c', '--configfile',default='config.cfg')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    p = parser.parse_args()
    configs = ini(p.configfile)
    
    if not 'mode' in configs:
        sys.stderr.write('mode missing from config (serial or tcp)\n')
        sys.exit(1)

    if configs['mode'] == 'tcp':
        interface = meshtastic.tcp_interface.TCPInterface(hostname = configs['host'])
    elif configs['mode'] == 'serial':
        interface = meshtastic.serial_interface.SerialInterface(devPath = configs['port'])
    else:
        sys.stderr.write('undefined interface\n')
        sys.exit(1)

    us = interface.getNode('^local')
    ouraddr = hex(us.nodeNum)[2:]
