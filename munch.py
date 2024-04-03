#!/usr/bin/env python3

def main():
    szamok = [str(n) for n in range(0,438579089)]
    e = 0
    osszeg = 0
    mennyi = 1
    for n in szamok:
        while e < len(n):
            osszeg += int(n[e]) ** int(n[e])
            e +=1
        e = 0
        if osszeg == int(n):
            mennyi += 1
        osszeg = 0
    print(mennyi)

if __name__ == '__main__':
    main()