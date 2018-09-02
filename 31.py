#!/usr/bin/env python3
def main():
    x=open('lines.txt','rt');y=open('lines-copy.txt','wt')
    for i in x:print(i.rstrip(),file=y)
    y.close()
if __name__=='__main__':main()
