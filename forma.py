#!/usr/bin/env python3

def main():
    #soulsborne first bosses 
    boss_info = [('demon\'s souls', 2009, 'phalanx',2.345),('dark souls 1', 2011, 'asylum demon',1.523),
                 ('dark souls 2', 2014, 'the last giant',2.842),('bloodborne', 2015, 'cleric beast',3.552),
                 ('dark souls 3', 2016, 'iudex gundyr',2.532),('sekiro', 2019, 'geniciro',4.713),
                 ('elden ring', 2022, 'margit',4.842),]
    

    print("{0:<16} {1:^18} {2:^20} {3:^20}".format("game title", "year developed", "first boss","10/ difficulty"))
    print("_"*80)
    for element in boss_info:
        print("{0:16} {1:^18} {2:^20} {3:^ 20.1f}".format(element[0], element[1],element[2],element[3]))

if __name__ == '__main__':
    main()