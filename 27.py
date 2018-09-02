#!/usr/bin/env python3
def main():
    try:x=int('foo')
    except ValueError:print('This is not a number!')
    try:y=4/0
    except ZeroDivisionError:print('You cannot divide by zero!')
    try:z=range(4,4,4,4)
    except:import sys;print('Unexpected error: {}'.format(sys.exc_info()))
if __name__ == '__main__': main()
