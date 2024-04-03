#!/usr/bin/env python3

def main():
    ekezet = {'á':'a', 'é':'e','ó':'o','ö':'o','ő':'o','ú':'u','ü':'u','ű':'u','í':'i','Á':'A','É':'E','Ó':'O','Ö':'O','Ő':'O','Ű':'U','Ú':'U','Ü':'U','Í':'I',}
    print(ekezet)
    TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""
    lista = TEXT
    e = 0
    for n,m in ekezet.items():
            while e < len(lista):
                if lista[e] == n:
                    lista= lista.replace(lista[e],m)
                e += 1
            e = 0
                
    print(lista)


if __name__ == '__main__':
    main()