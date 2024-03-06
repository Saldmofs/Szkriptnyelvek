#!/usr/bin/env python3

def main():
    num1 = input("Please give a number: ")
    num2 = input()
    if num1 == "" or num2 == "":
        print("error")
    else:
        print(int(num1)+int(num2))

if __name__ == '__main__':
    main()