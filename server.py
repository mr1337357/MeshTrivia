import sys
import time
import argparse
from pubsub import pub

import meshtastic
import meshtastic.tcp_interface
import meshtastic.serial_interface

import pypb
from ini import ini
from tdb import tdb
import trivialog

iface = None
db = None

dump = open('packets.dump','wb')

def onRecv(packet,interface):
    dec = None
    try:
        dec = packet['decoded']
    except:
        print('not decoded')
        return
    src = hex(packet['from'])[2:]
    dst = hex(packet['to'])[2:]
    match dec['portnum']:
        case 'NODEINFO_APP':
            print(dec['user'])
            user = dec['user']
            username = user['longName']
            uname = user['shortName']
            print(username)
            print(uname)
            db_user = db.get_user_by_address(src)
            if db_user == None:
                db.add_user(username,uname,src)
            else:
                print(db_user)
                
        case 'TEXT_MESSAGE_APP':
            id = packet['toId'][1:]
            if id == ouraddr:
                pass
        case _:
            print(dec['portnum'])
    
def onLoss(interface):
    pass
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='MeshTrivia', description='Trivia over MeshTastic')
    parser.add_argument('-c', '--configfile',default='config.cfg')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-l', '--logfile', default=None)
    p = parser.parse_args()
    logger = trivialog.instance(p.logfile,p.verbose)
    configs = ini(p.configfile)
    logger.log('starting MeshTrivia')
    
    pub.subscribe(onRecv, 'meshtastic.receive')
    pub.subscribe(onLoss, 'meshtastic.connection.lost')
    
    if configs['connection']['mode'] == 'tcp':
        iface = meshtastic.tcp_interface.TCPInterface(hostname = configs['connection']['host'])
    elif configs['connection']['mode'] == 'serial':
        iface = meshtastic.serial_interface.SerialInterface(devPath = configs['connection']['port'])
    else:
        sys.stderr.write('undefined interface\n')
        sys.exit(1)

    us = iface.getNode('^local')
    ouraddr = hex(us.nodeNum)[2:]
    db = tdb()
    print(iface)
    print(dir(iface))
    while True:
        time.sleep(1)