#!/usr/bin/env python3
def main():
    a=set(input('Enter a word: '))
    b=set(input('Enter another word: '))
    print('a   = ',end='');print_set(a)
    print('b   = ',end='');print_set(b)
    print('a&b = ',end='');print_set(a&b)
    print('a|b = ',end='');print_set(a|b)
    print('a^b = ',end='');print_set(a^b)
def print_set(o):
    print('{',end='')
    for x in o:print(x,end='')
    print('}')
if __name__ == '__main__': main()
