import sqlite3
import random

import trivialog

#_dbcon = None

class tdb():
    def __init__(self,db='trivia.db'):
        self.logger = trivialog.instance()
        self.con = sqlite3.connect(db)
        self.logger.log('starting trivia db',trivialog.LOGLEVEL_INFO)

    def create_tables(self):
        tables = { 'questions':['category', 'question', 'answer'],
                        'users': ['username', 'shortname', 'address', 'score']}
        cur = self.con.cursor()
        for name in tables:
            info = cur.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name = ? ',(name,)).fetchall()
            print(info)
            if len(info) == 0:
                self.logger.log('creating table {}'.format(name),trivialog.LOGLEVEL_INFO)
                cur.execute('CREATE TABLE {}({})'.format(name, ','.join(tables[name])))

    def get_user_by_address(self,addr):
        cur = self.con.cursor()
        info = cur.execute('SELECT username, shortname, score FROM users WHERE address = ?',(addr,))
        row = info.fetchone()
        return row
        
    def add_user(self,name,shortname,address):
        cur = self.con.cursor()
        cur.execute('INSERT INTO users (username, shortname, address, score) VALUES(?,?,?,0)',(name,shortname,address,))
        
    
    def get_user_by_name(self,name):
        pass
        

if __name__ == '__main__':
    a = tdb()
    a.create_tables()