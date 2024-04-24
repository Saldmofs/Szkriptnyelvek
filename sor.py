#!/usr/bin/env python3

from collections import deque

class Sor:
    def __init__(self):
        self.data = deque([])

    def betesz(self, elem):
        self.data.append(elem)

    #def beteszbal(self, elem):
     #   self.data.appendleft(elem)

    #def kivesz(self):
     #   if self.ures():
      #      return None
       # else:
        #    return self.data.pop()

    def kivesz(self):
        if self.ures():
            return None
        else:
            return self.data.popleft()

    def meret(self):
        return len(self.data)
    
    def ures(self):
        if self.meret() == 0:
            return True
        else:
            return False
        
    def __str__(self):
        return str(self.data)

def main():
    v = Sor()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

if __name__ == '__main__':
    main()