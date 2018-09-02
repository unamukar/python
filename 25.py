#!/usr/bin/env python3
class reverse(str):
    def __str__(self):return self[::-1]
def main():
    x=input('Enter a word: ');y=reverse(x);print(y)
if __name__ == '__main__': main()
