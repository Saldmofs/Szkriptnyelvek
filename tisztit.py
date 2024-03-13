#!/usr/bin/env python3

def tisztit(cls):

    return(''.join(cls.split()))


def main():
    szoveg =  "192.20.246.138:\n 6666"
    print(tisztit(szoveg))

if __name__ == '__main__':
    main()