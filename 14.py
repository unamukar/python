#!/usr/bin/env python3
def main():colors(R='Red',G='Green',B='Blue');colors()
def colors(**kwargs):
    if len(kwargs):
        for k in kwargs:print('{} means {}'.format(k,kwargs[k]))
        print()
    else: print('Black is black.')
if __name__=='__main__':main()
