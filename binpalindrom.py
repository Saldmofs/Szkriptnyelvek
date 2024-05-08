#!/usr/bin/env python3


def binpalindrom(num):
    eredmeny = 0
    for n in num:
        if str(n) == str(n)[::-1] and str(bin(n)[2:]) == str(bin(n)[2:])[::-1]:
            eredmeny += n
    return eredmeny

def main():
    num = range(1,1000001)
    print(binpalindrom(num))

if __name__ == '__main__':
    main()