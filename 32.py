#/usr/bin/env python3
def main():
    i=open('binary.dat','rb');o=open('binary-copy.dat','wb')
    while True:
        b=i.read(100000000)
        if b:o.write(b)
        else: break
    o.close()
if __name__=='__main__':main()
