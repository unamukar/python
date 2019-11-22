#!/usr/bin/env python3
import time
def elapsed_time(f):
    def wrapper():
        print('Here starts the wrapper')
        t1=time.time();f();t2=time.time()
        print('Elapsed time: {} ms'.format((t2-t1)*1000))
    return wrapper
@elapsed_time
def suma():
    n=[]
    for x in (range(0,100000)):n.append(x)
    print('Big sum: {}'.format(sum(n)))
def main():suma()
if __name__ == '__main__': main()
