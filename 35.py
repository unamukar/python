#!/usr/bin/env python3
import time2words
def main():
    lista=['11:55','22:22','03:03','00:15','23:45','08:45','12:50','14:00']
    lista2=['11:55']
    for x in lista:print('{} -> {}'.format(x,time2words.t2w(x)))
    for x in lista2:print('{} -> {}'.format(x,time2words.t2w(x)))
if __name__=='__main__':main()
