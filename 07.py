#!/usr/bin/env python3
def isprime(n):
    if n<=1:return False
    for x in range(2,n):
        if n%x==0:return False
    else:return True
def list(n):
    for x in range(n+1):
        if isprime(x):print(x,end=' ')
    print()
n=int(input('Please enter an integer: '))
if isprime(n):print('{} is prime:'.format(n));list(n)
else:print('{} is not prime'.format(n))
 
