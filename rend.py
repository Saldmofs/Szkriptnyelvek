#!/usr/bin/env python3

def Sort_Tuple(tup,i):
    tup.sort(key = lambda x: x[i])
    return tup

def Sort_List(users):
    users2 = []
    users3 = []
    for n in users:
        users2.append(n.split(":")[0])
    users2.sort(reverse = True)
    for n in users2:
        for m in users:
            if n == m.split(":")[0]:
                users3.append(m)
    return users3

def Sort_Matrix(matrix):
    matrix.sort(key = lambda x: x[1])
    return matrix

def main():
    data = [ 
    (1, 'Albany', 'NY', 162692),
    (121, 'Wyoming', 'NY', 8722),
    (3, 'Allegany', 'NY', 11986),
    (123, 'Yates', 'NY', 5094)
    ]

    print(Sort_Tuple(data,3))

    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']

    print(Sort_List(users))

    matrix = [ [2, 6], [1, 3], [5, 4] ]
    
    print(Sort_Matrix(matrix))



if __name__ == '__main__':
    main()