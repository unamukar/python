#!/usr/bin/env python3
import time2words
def main():
    #lista=['11:55','03:03','00:15','23:45','08:45','12:50','14:00']
    #lista2=['11:55']
    lista=['22','88','7','90','323','409','999','45223','234343','100001','999999','990099']
    for x in lista:print('{} -> {}'.format(x,time2words.m2w(x)))
if __name__=='__main__':main()
