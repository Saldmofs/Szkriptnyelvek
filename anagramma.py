#!/usr/bin/env python3

def normalize(wrd):
    wrd = wrd.replace(" ","")
    return ''.join(wrd.lower())


def main():

    str1 = input("adjon meg 2 stringet ")
    str2 = input()
    lista1 = list(normalize(str1))
    lista1.sort()
    lista2 = list(normalize(str2))
    lista2.sort()

    if lista1 == lista2:
        print("anagramma")
    else:
        print("nem anagramma")

if __name__ == '__main__':
    main()