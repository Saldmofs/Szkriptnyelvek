#!/usr/bin/env python3



def main():
    a = "abcde"
    print (a[0:(len(a)-(len(a)//2))])
    print (a[(len(a)-(len(a)//2)):])
    print (3//2)
    print (a[3:])

if __name__ == '__main__':
    main()