#!/usr/bin/env python3

def main():
    lista = []
    osszeg = 0
    
    with open("szamok.txt","r") as szamok:
        for sor in szamok:
            lista.append(sor)
    for n in lista:
        szamok = n.split()
        maxszam = float("-inf")
        minszam = float("inf")
        for e in szamok:
            if int(e) < minszam:
                minszam = int(e)
            if int(e) > maxszam:
                maxszam = int(e)
        osszeg += maxszam - minszam

    print(osszeg)






if __name__ == '__main__':
    main()