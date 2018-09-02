#!/usr/bin/env python3
def main():numbers={'one':'uno','two':'dos','three':'tres'};print_dict(numbers)
def print_dict(o):
    for x in o:print('{}: {}'.format(x,o[x]))
if __name__=='__main__':main()
