#!/usr/bin/env python3

def zarojel(m):
    zarojel = "({[}])"
    zarojelek = {')':'(',']':'[','}':'{'}
    lista = []
    igaz = True
    e = 0
    i = 0
    for n in m:
        if n in zarojel:
            lista.append(n)
    if len(lista)%2 == 0:
        while e < len(lista)//2:
            if lista[e] is not zarojelek[lista[i-1]]:
                igaz = False
            e += 1
            i -= 1
    else:
        igaz = False
    return igaz

def main():
    print(zarojel("{[(3+1)+2]+}"))
if __name__ == '__main__':
    main()