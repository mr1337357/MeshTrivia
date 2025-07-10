from inspect import currentframe, getframeinfo
import os
import sys
import time

LOGLEVEL_ERR=0
LOGLEVEL_WARN=1
LOGLEVEL_INFO=2
LOGLEVEL_DEBUG=3

_instance = None

class trivialog:
    def __init__(self,logfile=None,loglevel=LOGLEVEL_ERR):
        self.here = os.getcwd()
        if logfile != None:
            self.outfile = open(logfile,'w')
        else:
            self.outfile = sys.stderr
        self.loglevel = loglevel
        
    def set_loglevel(self,level):
        self.loglevel = level
        
    def log(self,message,level=LOGLEVEL_INFO):
        if level > self.loglevel:
            return
        caller = currentframe().f_back
        info = getframeinfo(caller)
        fn = info.filename
        ln = info.lineno
        if fn.startswith(self.here):
            fn = fn[len(self.here)+1:]
        now = time.clock_gettime(time.CLOCK_REALTIME)
        self.outfile.write('[{:.2f}]{}({}): {}\n'.format(now,fn,ln,message))
        
def instance(logfile=None,loglevel=LOGLEVEL_ERR):
    global _instance
    if _instance == None:
        _instance = trivialog(logfile,loglevel)
    return _instance