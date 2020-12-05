# Advent of code 2020 day 5 challenges

import math

with open('Day5input.txt') as f:
    lines = f.read().splitlines() #read lines from txt into list

#boarding passes for testing
'''
FBFBBFFRLR
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
'''

def decodePass(code):
    rowDown, rowUp = 0, 127
    colDown, colUp = 0, 7
    for c in code:
        if c == 'F': 
            rowUp = math.floor(rowUp - ((rowUp - rowDown) / 2))
        if c == 'B':
            rowDown = math.ceil(rowDown + ((rowUp - rowDown) / 2))
        if c == 'L':
            colUp = math.floor(colUp - ((colUp - colDown) / 2))
        if c == 'R':
            colDown = math.ceil(colUp - ((colUp - colDown)) / 2)
    row,col = rowDown,colDown
    return row * 8 + col

def findMissingSeat(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst][0]

#make list of seat IDs from list of boarding passes, sort by ascending values
lst = []
for code in lines:
    codeID = decodePass(code)
    lst.append(codeID)
lst.sort()


print('Part 1: Highest Seat ID: ', lst[-1])
print('Part 2: Your Seat: ',findMissingSeat(lst))


#simplify code. Formulas to variables?


    