#!/usr/bin/env python3

from enum import Enum,auto

class hangrendenum(Enum):
    MELY = "aáoóuú"
    MAGAS = "eéiíöőüű"
    VEGYES = auto()
    SEMMILYEN = auto()
    def hangrend(szo):
        mely = False
        magas = False

        for n in szo:
            for me in hangrendenum.MELY.value:
                if n == me:
                    mely = True
            for ma in hangrendenum.MAGAS.value:
                if n == ma:
                    magas = True

        if mely and magas:
            return hangrendenum.VEGYES.name
        elif mely:
            return hangrendenum.MELY.name
        elif magas:
            return hangrendenum.MAGAS.name
        else:
            return hangrendenum.SEMMILYEN.name



def main():
    szo = input("Szó: ")
    print(f"{szo} hangrendje: {hangrendenum.hangrend(szo)}")
    
    
if __name__ == "__main__":
    main()