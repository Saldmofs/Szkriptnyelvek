#!/usr/bin/env python3

def main():

    sakk = ['|', ' .', ' .', ' .', ' .', ' .', ' .', ' .', ' .',' |']
    tabla = []
    c = 0
    sor = ""
    index = 0
    queen = [7,3,0,2,5,1,6,4]

    for n in sakk:
        sor += n

    while c < 8:
        tabla.append(sor)
        c += 1
    c = 1

    for n in queen:
        index = 7-n
        tabla[index] = tabla[index].split(" ")
        tabla[index][c] = "Q"
        tabla[index] =' '.join(tabla[index])
        c+=1
    c = 0

    print("+"+"-"*17+"+")
    for n in tabla:
        print(n)
    print("+"+"-"*17+"+")
if __name__ == '__main__':
    main()