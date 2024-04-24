#!/usr/bin/env python3

class myQueue:


    def __init__(self):
        self.verem1 = []
        self.verem2 = []

    def betesz(self,elem):
        self.verem1.append(elem)

    def kivesz(self):
        n = len(self.verem1)-1
        while n >= 0:              
            self.verem2.append(self.verem1[n])
            n-=1
        n = len(self.verem2)-2

        self.verem1.clear()

        kiir = self.verem2.pop()

        while n >= 0:
            self.verem1.append(self.verem2[n])
            n-=1
        n = len(self.verem1)-1

        self.verem2.clear()

        return kiir
    

    def meret(self):
        return len(self.verem1)
    
    def ures(self):
        if self.meret() == 0:
            return True
        else:
            return False

    
    def __str__(self):
        return f"{self.verem1}"

        
        

def main():
    a = myQueue()
    print(a)
    print(a.ures())
    print(a.meret())
    a.betesz(1)
    a.betesz(2)
    a.betesz(3)
    print(a)
    print(a.ures())
    print(a.meret())
    x = a.kivesz()
    print(x)
    print(a)
    a.kivesz()
    print(a)


if __name__ == '__main__':
    main()