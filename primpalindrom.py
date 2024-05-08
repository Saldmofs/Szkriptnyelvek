#!/usr/bin/env python3

from prim import is_prime_mr

def palindromesprim(num):
    while True:    
        if str(num) == str(num)[::-1] and is_prime_mr(num):
            return num
        else:
            num += 1
    
        


def main():

    print(palindromesprim(31))
    print(palindromesprim(130))
    print(palindromesprim(131))
    print(palindromesprim(1977))

if __name__ == '__main__':
    main()