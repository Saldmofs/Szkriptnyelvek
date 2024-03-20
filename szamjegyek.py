#!/usr/bin/env python3

def main():
    lista = range(1,101)
    i = 0
    n = 0
    sum = 0
    while i < len(lista):
        while n < len(str(lista[i])):
            temp = str(lista[i])
            sum += int(temp[n])
            n += 1
        n = 0
        i += 1
    print(list(lista))
    print(sum)

if __name__ == '__main__':
    main()