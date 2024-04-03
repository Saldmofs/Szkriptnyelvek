#!/usr/bin/env python3

def main():
    osszeg = 0
    hatvany = 2**1000
    for n in str(hatvany):
        osszeg += int(n)
    print(osszeg)

if __name__ == '__main__':
    main()