# Author: Wenrui Zhang wkz5094@psu.edu
# GitHub ID: 2020nini

"""
Your program should read in a pickle file that encodes a sudoku puzzle,
print out a puzzle, and analyze possible answers for a given coordinate
(x,y).
$python3 sudoku.py sudokus/s01a.p1 3 5 answer.csv
$python3 sudoku.py sudokus/s01a.p1 0 1 answer.csv
"""
import sys
import pickle
import csv


def get_data(i,j,lines):
    total_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in lines[i]:
        if num in total_num:
            total_num.remove(num)
    for index in range(9):
        if lines[index][j] in total_num:
            total_num.remove(lines[index][j])
    arroud_list = []
    if i in [0,3,6]:
        i = i + 1
    elif i in [2,5,8]:
        i = i - 1

    if j in [0, 3, 6]:
        j = j + 1
    elif j in [2, 5, 8]:
        j = j - 1
    arroud_list = [lines[i][j], lines[i-1][j], lines[i+1][j],
                       lines[i][j-1], lines[i-1][j-1], lines[i+1][j-1],
                       lines[i][j+1],lines[i-1][j+1],lines[i+1][j+1]]
    for num in arroud_list:
        if num in total_num:
            total_num.remove(num)
    return str(total_num)


if __name__ == "__main__":
    file = sys.argv[1]
    with open(file, 'rb') as f:
        lines = pickle.load(f)

    lines_ = []
    for line in lines:
        print(" ".join("{0}".format(n) for n in line))
        lines_.append(line)
    row_num = int(sys.argv[2])
    col_num = int(sys.argv[3])

    for i in range(9):
        for j in range(9):
            lines_[i][j] = int(lines_[i][j])
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

    if lines_[row_num][col_num] !=0:
        print("(%s,%s)[%s]" % (row_num, col_num, lines_[row_num][col_num]))
    else:
        print("(%s,%s) %s" % (row_num, col_num, get_data(row_num, col_num, lines_)))
    save_file = sys.argv[4]

    with open(save_file, 'w+') as f:
        spamwriter = csv.writer(f, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['row', 'column', 'numbers'])
        for i in range(9):
            for j in range(9):
                if lines_[i][j] == 0:
                    res = get_data(i, j, lines_)
                    spamwriter.writerow([i, j, res])