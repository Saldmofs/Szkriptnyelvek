#!/usr/bin/env python3

def main():
    with open('string1.py','r') as f1, open('string1_clean.py','w') as f2:
        for line in f1:
            if line.strip().startswith("#") == False:
                f2.write(line)

if __name__ == '__main__':
    main()