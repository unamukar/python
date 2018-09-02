#!/usr/bin/env python3
import sqlite3
class db:
    def __init__(self,dbname):
        if dbname:self._dbname=dbname
        self._dbfile=sqlite3.connect(self.dbname())
        self.dbfile().row_factory=sqlite3.Row
    def dbfile(self):return self._dbfile
    def dbname(self,n=None):
        if n:self._dbname=n
        try:return self._dbname
        except AttributeError:return 'unknown'
    def close(self):self.dbfile().close()
    def sql(self,q,p=()):
        s=self.dbfile()
        x=s.execute(q,p)
        s.commit()
        if x:return x
    def insert(self,t,x):
        k=sorted(x.keys())
        v=[x[i] for i in k]
        m='INSERT INTO {} ({}) VALUES ({})'
        q=m.format(t,','.join(k),','.join('?'*len(v)))
        self.sql(q,v)
    def drop(self,t):
        self.sql('DROP TABLE IF EXISTS {}'.format(t))
    def create(self,t,p):
        P='(id INTEGER PRIMARY KEY'
        for x in sorted(p):P=P+','+x+' '+p[x]
        P=P+')'
        m='CREATE TABLE {} {}'
        self.sql(m.format(t,P))
