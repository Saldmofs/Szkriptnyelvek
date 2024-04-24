#!/usr/bin/env python3
import math

class Sphere:

    def __init__(self, r):
        self.r = r

    def volume(self):
        return (4/3) * math.pi * (self.r**3)
    
    def surface(self):
        return 4 * math.pi * (self.r**2)
    
    def __eq__(self,other):
        return self.volume() == other.volume()
    
    def __ne__(self,other):
        return self.volume() != other.volume()
    
    def __lt__(self,other):
        return self.volume() < other.volume()
    
    def __gt__(self,other):
        return self.volume() > other.volume()
    
    def __le__(self,other):
        return self.volume() <= other.volume()
    
    def __ge__(self,other):
        return self.volume() >= other.volume()
    
    def __str__(self):
        return str(self.data)
    

class Ellipsoid:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return (4/3) * math.pi * self.a * self.b * self.c
    
    def surface(self):
        one = self.a*self.b
        two = self.a*self.c
        three = self.b*self.c
        return 4*math.pi*(((one**1.6)+(two**1.6)+(three**1.6))/3)**(1/1.6)
    
    def __str__(self):
        return f"{self.a}{self.b}{self.c}"

def main():

    a1 = Sphere(5)
    a2 = Sphere(6)
    print(a1 == a2)

if __name__ == '__main__':
    main()