#!/usr/bin/env python3

def main():
    szaz = range(1,101)
    temp = 0
    for i in szaz:
        temp += int(i)
    ossznegyzet = temp * temp
    print("elso 100 szam osszegenek negyzete: ",ossznegyzet)
    temp = 0
    for i in szaz:
        temp += int(i) * int(i)
    negyzetossz = temp
    print("elso 100 szam negyzetenek osszege: ",negyzetossz)

    print("kulonbseguk: ", ossznegyzet - negyzetossz)

if __name__ == '__main__':
    main()