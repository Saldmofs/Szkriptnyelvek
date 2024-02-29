#!/usr/bin/env python3
import math

def main():
    print("Hello world")

    a = input()
    a = int(a)
    b = input()
    b = int(b)
    mennyi = 1
    osztva = 0
    eredmeny1 = 0
    eredmeny2 = 0


    while True:
        if a % b == 0:
            print(f"legn k o: {str(b)}" )
            x = (osztva * 0) +1
            y = (osztva *1) +0
            eredmeny1 = pow(-1, mennyi) * x
            eredmeny2 = pow(-1, mennyi+1) * y
            print(f"x: {eredmeny1}" )
            print(f"y: {eredmeny2}" )
            print(f"mennyi: {mennyi}" )
            print(f"oszva: {osztva}" )
            break
        else:
            mennyi += 1
            osztva = a / b
            c = a % b
            a = b
            b = c

if __name__ == '__main__':
    main()