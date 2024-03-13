#!/usr/bin/env python3

def szorzat(lista):
    eredmeny = 1
    for n in lista:
        eredmeny = eredmeny *n
    return eredmeny


def main():
    lista = [1,2,3]
    print(szorzat(lista))


if __name__ == '__main__':
    main()