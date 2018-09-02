#!/usr/bin/env python3
def main():colors('Red','Green','Blue');colors()
def colors(*args):
    if len(args):
        for s in args:print(s,end=' ')
        print()
    else: print('Black')
if __name__=='__main__':main()
