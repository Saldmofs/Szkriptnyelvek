#!/usr/bin/env python3
import sys
import random as r

UPTO = 100


def main():
    i = 0
    for i in range(UPTO):
        if i % 10 == 0:
            print()
        print(r.randint(0, 9), end="")
    print()

if __name__ == '__main__':
    main()