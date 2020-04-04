import numpy as np

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def isPossibleToPlaceNumberAtThisLocation(row, column, number):
    global grid
    for i in range(0, 9):
        if grid[row][i] == number:
            return False;
    for i in range(0, 9):
        if grid[i][column] == number:
            return False;
    rowGroup = (row // 3) * 3
    columnGroup = (column // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[rowGroup + i][columnGroup + i] == number:
                return False
    return True


def solveIt():
    global grid
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if isPossibleToPlaceNumberAtThisLocation(row, column, number):
                        grid[row][column] = number
                        solveIt()
                        grid[row][column] = 0
                return
    print (np.matrix(grid))
    input("More")

solveIt()
