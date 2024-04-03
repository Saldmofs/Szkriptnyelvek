#!/usr/bin/env python3


def main():
    test = [1,300,2,200,1]
    hossz = len(test)
    test.sort()
    if len(test) % 2 == 1:
        medi = test[hossz//2]
    else:
        medi = (test[int(hossz/2)-1] + test[int(hossz/2)])/2
    print(medi)

if __name__ == '__main__':
    main()