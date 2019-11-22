#!/usr/bin/env python3
from math import pi
def main():
    x=int(input('Maximum number: '))
    s=range(x)
    a=[x*2 for x in s]
    b=[x for x in s if x%3==0]
    c=[round(pi,i)for i in s]
    d={x:x**2 for x in s if x not in b}
    print_list(s)
    print_list(a)
    print_list(b)
    print_list(c)
    print(d)
def print_list(o):
    for x in o:print(x,end = ' ')
    print()
    C=[round(pi,2)]
    print(C)
if __name__ == '__main__': main()
