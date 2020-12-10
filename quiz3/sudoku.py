# Author: Wenrui Zhang wkz5094@psu.edu
# GitHub ID: 2020nini

"""
Your program should read in a pickle file that encodes a sudoku puzzle,
print out a puzzle, and analyze possible answers for a given coordinate
(x,y).
$python3 sudoku.py sudokus/s01a.p1 3 5 answer.csv
$python3 sudoku.py sudokus/s01a.p1 0 1 answer.csv
"""
import numpy as np

 
def nine(data):
    nine_block = np.zeros([3,3,3,3], dtype = int)
    for i in range(3):
        for j in range(3):
            nine_block[i,j] = data[3*i:3*(i+1),3*j:3*(j+1)]
    return nine_block
 
def num_set(data, nine_block):
    pick_set = {}
    for i in range(9):
        for j in range(9):
            if data[i,j] == 0:
                pick_set[str(i)+str(j)] = set(np.array(range(10))) - \
                (set(data[i,:]) | set(data[:,j]) | \
                set(nine_block[i//3,j//3].ravel()))
    return pick_set
 
def try_insert(data):    
 
    insert_step = []
    while True:
        
        pick_set = num_set(data, nine(data))
        if len(pick_set) == 0: break
        pick_sort = sorted(pick_set.items(), key = lambda x:len(x[1]))
        item_min = pick_sort[0]
        key = item_min[0]
        value = list(item_min[1])
        insert_step.append((key, value))
        if len(value) != 0:
            data[int(key[0]), int(key[1])] = value[0]
        else:
            insert_step.pop()
            for i in range(len(insert_step)):
                huishuo = insert_step.pop()
                key = huishuo[0]
                insert_num = huishuo[1]
                if len(insert_num) == 1:
                    data[int(key[0]), int(key[1])] = 0
                else:
                    data[int(key[0]), int(key[1])] = insert_num[1]
                    insert_step.append((key, insert_num[1:]))
                    break
    print(data)    

if __name__ == '__main__':

    
    data = '0 4 0 0 0 0 1 7 9\
            0 0 2 0 0 8 0 5 4\
            0 0 6 0 0 5 0 0 8\
            0 8 0 0 7 0 9 1 0\
            0 5 0 0 9 0 0 3 0\
            0 1 9 0 6 0 0 4 0\
            3 0 0 4 0 0 7 0 0\
            5 7 0 1 0 0 2 0 0\
            9 2 8 0 0 0 0 6 0'
    
    
    data = np.array(data.split(), dtype = int).reshape((9, 9))
    print(data)
    try_insert(data)