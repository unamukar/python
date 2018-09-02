#!/usr/bin/env python3
import dbSebas
def main():
    n='37.db'
    t='numbers'
    t2='colors'
    t3='animals'
    p=dict(English='TEXT',Spanish='TEXT')
    p3=dict(English='TEXT',Spanish='TEXT',Catalan='TEXT')
    x=[dict(English='one',Spanish='uno'),dict(English='two',Spanish='dos')]
    x2=[dict(English='red',Spanish='rojo')]
    z1=[dict(English='dog',Spanish='perro',Catalan='ca')]
    z2=[dict(English='cat',Spanish='gato',Catalan='moix')]
    d=dbSebas.db(n)
    d.drop(t)
    d.drop(t2)
    d.drop(t3)
    d.create(t,p)
    d.create(t2,p)
    d.create(t3,p3)
    for i in x:d.insert(t,i)
    for i in x2:d.insert(t2,i)
    for i in z1:d.insert(t3,i)
    for i in z2:d.insert(t3,i)
    for i in d.sql('SELECT * FROM {}'.format(t)):print('Table {}: {}'.format(t,dict(i)))
    for i in d.sql('SELECT * FROM {}'.format(t2)):print('Table {}: {}'.format(t2,tuple(i)))
    for i in d.sql('SELECT * FROM {}'.format(t2)):print('Table {}: {}'.format(t2,list(i)))
    for i in d.sql('SELECT * FROM {}'.format(t2)):print('Table {}: {}'.format(t2,set(i)))
    for i in d.sql('SELECT * FROM {}'.format(t2)):print('Table {}: {}'.format(t2,dict(i)))
    for i in d.sql('SELECT * FROM {}'.format(t3)):print('Table {}: {}'.format(t3,tuple(i)))
    for i in d.sql('SELECT * FROM {}'.format(t3)):print('Table {}: {}'.format(t3,list(i)))
    for i in d.sql('SELECT * FROM {}'.format(t3)):print('Table {}: {}'.format(t3,set(i)))
    for i in d.sql('SELECT * FROM {}'.format(t3)):print('Table {}: {}'.format(t3,dict(i)))
    d.close()
if __name__=='__main__':main()
