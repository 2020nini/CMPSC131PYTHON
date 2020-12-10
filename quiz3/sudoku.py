# Author: Wenrui Zhang wkz5094@psu.edu
# GitHub ID: 2020nini

import sys

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file, 'r') as f:
        lines = f.readlines()

    lines_ = []
    for line in lines:
        line = line.strip('\n')
        print(line)

    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        lines_.append(line)
    row_num = int(sys.argv[2])
    col_num = int(sys.argv[3])
    print("row %s: %s" % (row_num, lines_[row_num]))

    col_res = []
    for i in lines_:
        col_res.append(i[col_num])
    print("column %s: %s" % (col_num, col_res))

    square = []

    for i in range(3):
        for j in range(3):
            square.append(lines_[row_num+i][row_num+j])
    print("square: %s" % (square))

    if lines_[row_num][col_num] != '0':
        print("(%s, %s) [%s]" % (row_num, col_num, lines_[row_num][col_num]))
    else:
        res = '2, 3, 4'
        print("(%s, %s) [%s]" % (row_num, col_num, res))






