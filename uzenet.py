#!/usr/bin/env python3

def decode(mess):
    new = ""
    for n in mess:
        if ord(n) >= 65 and ord(n) <= 90 or ord(n) >= 97 and ord(n) <= 122:
            if ord(n) >= 89 and ord(n) <= 90:
                new += chr(ord(n)-24)
            elif ord(n) >= 121 and ord(n) <= 122:
                new += chr(ord(n)-24)
            else:
                new += chr(ord(n)+2)
        else:
            new += n
    return new
                

def main():
    mess = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

    print(decode(mess))

if __name__ == '__main__':
    main()