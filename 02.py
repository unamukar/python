#!/usr/bin/env python3
x=input('x = ');y=input('y = ')
m='x is {} and y is {}'.format(x,y)
if x==y:print('x = y : ',m)
elif x<y:print('x < y : ',m)
else:print('x > y : ',m)
