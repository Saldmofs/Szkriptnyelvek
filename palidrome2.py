#!/usr/bin/env python3

def palindrom(word):
    if word == word[::-1]:
        return "palindróm"
    else:
        return "nem palindróm"
    
def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])


def main():
    print(ispalindrome("gorog"))

if __name__ == '__main__':
    main()