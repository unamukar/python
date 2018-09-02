#!/usr/bin/env python3
class Duck:
    look='Looks like a duck.'
    walk='Walks like a duck.'
    def L(self):print(self.look)
    def W(self):print(self.walk)
def main():
    print('Donald:');Donald=Duck();Donald.L();Donald.W()
if __name__=='__main__':main()
