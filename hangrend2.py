#!/usr/bin/env python3

from enum import Enum,auto

class Hangrend(Enum):
    MELY = "aáoóuú"
    MAGAS = "eéiíöőüű"
    VEGYES = auto()
    SEMMILYEN = auto()
    
    def hangrend(szo):
        mely = False
        magas = False

        for n in szo:
            for e in Hangrend.MELY.value:
                if n == e:
                    mely = True
            for e in Hangrend.MAGAS.value:
                if n == e:
                    magas = True

        if mely and magas:
            return Hangrend.VEGYES.name
        elif mely:
            return Hangrend.MELY.name
        elif magas:
            return Hangrend.MAGAS.name
        else:
            return Hangrend.SEMMILYEN.name



def main():
    szo = input("Szó: ")
    print(f"{szo} hangrendje: {Hangrend.hangrend(szo)}")
    
    
if __name__ == "__main__":
    main()
