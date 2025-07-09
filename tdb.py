import sqlite3
import random

#_dbcon = None

class tdb():
    def __init__(self,db='trivia.db'):
        self.con = sqlite3.connect(db)
        print(globals())

    def create_tables(self):
        tables = { 'questions':['category','question','answer'],
                        'users': ['username', 'address', 'score']}
        cur = self.con.cursor()
        for name in tables:
            info = cur.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name = ? ',(name,)).fetchall()
            print(info)
            if len(info) == 0:
                cur.execute('CREATE TABLE ' + name + '(' + ','.join(tables[name])+')')

if __name__ == '__main__':
    a = tdb()
    a.create_tables()