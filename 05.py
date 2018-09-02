#!/usr/bin/env python3
numbers=['one','two','three']
print();print(type(numbers))
for x in numbers:print(x,end=' ')
numbers=range(3)
print();print(type(numbers))
for x in numbers:print(x,end=' ')
print()
for i in range(3):print(id(numbers[i]),end=' ')
numbers=list(range(3))
print();print(type(numbers))
for x in numbers:print(x,end=' ')
print()
for i in range(3):print(id(numbers[i]),end=' ')
for x in numbers:numbers[x]=x+1
print();print(type(numbers))
for x in numbers:print(x,end=' ')
print()
for i in range(3):print(id(numbers[i]),end=' ')
numbers={1:'one',2:'two',3:'three'}
print();print(type(numbers))
for x,y in sorted(numbers.items()):
    print('key:{} value:{}'.format(x,y))
for x in numbers:numbers[x]=numbers[x].upper()
print(type(numbers))
for x,y in sorted(numbers.items()):
    print('key:{} value:{}'.format(x,y))
