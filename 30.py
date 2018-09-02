#!/usr/bin/env python3
def main():
    f=open('lines.txt')
    for l in f:print(l.rstrip())
if __name__=='__main__':main()
