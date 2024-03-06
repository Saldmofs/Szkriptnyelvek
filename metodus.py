#!/usr/bin/env python3

#ez a függvény a whitespace karaktereket levágja a string elejéről és a végéről

def main():
    name = input("Name: ")
    print(f"Hello {name.strip()}")

if __name__ == '__main__':
    main()