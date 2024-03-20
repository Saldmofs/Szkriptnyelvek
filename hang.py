#!/usr/bin/env python3

def hangrend(word):
    mely = 'aáoóuú'
    magas = 'eéiíöőüű'
    ma = 0
    me = 0

    """if mely in word and magas not in word:
        return "mely"
    elif mely not in word and magas in word:
        return "magas"
    elif mely in word and magas in word:
        return "vegyes"
    else:
        return "semmilyen" """
    



    for i in word:
        if i in mely:
            me += 1
        elif i in magas:
            ma += 1
    if ma > 0 and me == 0:
        return "magas"
    elif me > 0 and ma == 0:
        return "mely"
    elif ma > 0 and me > 0:
        return "vegyes"
    else:
        return "semmilyen" 


    


def main():
    word = str(input("adjon megy egy szót"))
    print(hangrend(word))

if __name__ == '__main__':
    main()