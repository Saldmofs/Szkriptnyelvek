#!/usr/bin/env python3

def diamond(h):
    n = 1
    while n < h:
        valami = "*"*n
        print(valami.center(100))
        n += 2
    while n > 0:
        valami = "*"*n
        print(valami.center(100))
        n -= 2

def main():
    h = int(input("Adja meg a magasságot: "))
    if h % 2 == 0:
        print("egy páratlan számot adjon meg")
    else:
        diamond(h)

if __name__ == '__main__':
    main()