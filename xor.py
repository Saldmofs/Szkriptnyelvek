#!/usr/bin/env python3

def main():
    str1 = input("Str1: ")
    str2 = input("Str2: ")
    if bool(str1) != bool(str2):
        print("ok")
    else:
        print("not ok")


if __name__ == '__main__':
    main()