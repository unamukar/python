#!/usr/bin/env python3
def f(n='(default value)'):
    print('You wrote',n)
    return n
x=input('What to print: ')
f()
y=f(x)
print('Output: ',y)
