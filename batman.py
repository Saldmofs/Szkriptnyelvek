#!/usr/bin/env python3

import sys

def hello(s):
    if(s == "Batman"):
        print("Denever veszely")
    else:
        print(f"Hello{s}")

def main():
    nev = sys.argv[1]
    hello(nev)

if __name__ == '__main__':
    main()