#!/usr/bin/env python3

def main():
    num = input("Please give an int number: ")
    num = int(str(num)[::-1]) 
    print(num)

if __name__ == '__main__':
    main()