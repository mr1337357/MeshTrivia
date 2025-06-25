import sqlite3
import random

class questiondb():
    def __init__(self,db='questions.db'):
        self.con = sqlite3.connect(db)
        
    
class scoredb():
    def __init__(self,db='scores.db'):
        self.con = sqlite3.connect(db)


