import sys
import time
import argparse
from pubsub import pub

import meshtastic
import meshtastic.tcp_interface
import meshtastic.serial_interface

from ini import ini

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='MeshTrivia', description='Trivia over MeshTastic')
    parser.add_argument('-c', '--configfile',default='config.cfg')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    p = parser.parse_args()
    configs = ini(p.configfile)
    print(configs)
