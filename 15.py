#!/usr/bin/env python3
def main():
    x=int(input('Maximum number to show: '))
    for i in inclusive_range(x):print(i,end = ' ')
    print()
def inclusive_range(*args):
    n=len(args);start=0;step=1
    if n<1:raise TypeError('Expected at least 1 argument but got {}'.format(n))
    elif n==1:stop=args[0]
    elif n==2:(start,stop)=args
    elif n==3:(start,stop,step)=args
    else:raise TypeError('Expected at most 3 arguments but got {}'.format(n))
    i=start
    while i<=stop:yield i;i+=step
if __name__ == '__main__': main()
