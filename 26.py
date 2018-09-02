#!/usr/bin/env python3
class inclusive_range:
    def __init__(self,*args):
        n=len(args);self._start=0;self._step=1
        if n<1:raise TypeError('expected at least 1 argument, got {}'.format(n))
        elif n==1:self._stop=args[0]
        elif n==2:(self._start,self._stop)=args
        elif n==3:(self._start,self._stop,self._step)=args
        else:raise TypeError('expected at most 3 arguments, got {}'.format(n))
        self._next=self._start
    def __iter__(self):return self
    def __next__(self):
        if self._next>self._stop:raise StopIteration
        else:_r=self._next;self._next+=self._step;return _r
def main():
    for n in inclusive_range(10):print(n,end=' ')
    print()
if __name__ == '__main__': main()
