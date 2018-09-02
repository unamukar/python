#!/usr/bin/env python3
import sqlite3
def main():
    d=sqlite3.connect('36.db')
    c=d.cursor()
    c.execute("DROP TABLE IF EXISTS numbers")
    c.execute("CREATE TABLE numbers (id INTEGER PRIMARY KEY,english TEXT,spanish TEXT)")
    c.execute("INSERT INTO numbers (english,spanish) VALUES ('one','uno')")
    c.execute("INSERT INTO numbers (english,spanish) VALUES ('two','dos')")
    c.execute("INSERT INTO numbers (english,spanish) VALUES ('three','tres')")
    d.commit()
    c.execute("SELECT COUNT(*) FROM numbers")
    print('There are {} rows in the table.'.format(c.fetchone()[0]))
    for r in c.execute("SELECT * FROM numbers"):print(r)
    c.execute("DROP TABLE numbers")
    d.close()
if __name__=='__main__':main()
