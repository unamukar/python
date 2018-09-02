#!/usr/bin/env python3
clouded=input('Is it clouded?(y/n): ')
a='It might rain.'
b='It is sunny.'
x=a if clouded=='y' else b
print(x)
n=int(input('How many items are there in the box? '))
a='The box is not empty.'
b='It is empty.'
x=a if n else b
print(x)
