#!/usr/bin/env python3
def inclusive_range(*args):
    n=len(args);start=0;step=1
    if n<1:raise TypeError('expected at least 1 argument, got {}'.format(n))
    elif n==1:stop=args[0]
    elif n==2:(start,stop)=args
    elif n==3:(start,stop,step)=args
    else:raise TypeError('expected at most 3 arguments, got {}'.format(n))
    i=start
    while i<=stop:yield i;i+=step
def main():
    try:
        for i in inclusive_range(25):print(i,end=' ')
        print()
    except TypeError as e:print('inclusive_range error: {}'.format(e))
    try:
        for i in inclusive_range():print(i,end=' ')
        print()
    except TypeError as e:print('inclusive_range error: {}'.format(e))
    try:
        for i in inclusive_range(4,4,4,4):print(i,end=' ')
        print()
    except TypeError as e:print('inclusive_range error: {}'.format(e))
    for i in inclusive_range(4,4,4,4):print(i,end=' ')
if __name__ == '__main__': main()
