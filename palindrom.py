#!/usr/bin/env python3


def main():
    word = input("Please give a word: ")
    if word == word[::-1]:
        print("it is a palindrome")
    else:
        print("it's not a palindrome")

if __name__ == '__main__':
    main()