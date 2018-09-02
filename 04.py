#!/usr/bin/env python3
a=0;b=1;M=int(input('Fibonacci max number: '))
while b<M:print(b,end=' ');c=b;b=a+b;a=c
print()
