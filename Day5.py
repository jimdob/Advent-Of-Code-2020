# Advent of code 2020 day 5 challenges

import math

with open('Day5input.txt') as f:
    lines = f.read().splitlines() #read lines from txt into list

print(len(lines))
print(max(lines, key=len))
print(min(lines, key=len))
print(lines[0])

#test passes
'''
FBFBBFFRLR
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
'''


def decodePass(code):
    rowDown, rowUp = 0, 127
    colDown, colUp = 0, 7
    print(rowDown, rowUp)
    for c in code:
        if c == 'F': 
            rowUp = math.floor(rowUp - ((rowUp - rowDown) / 2))
            print(c,rowDown,rowUp)
        if c == 'B':
            rowDown = math.ceil(rowDown + ((rowUp - rowDown) / 2))
            print(c,rowDown, rowUp)
        if c == 'L':
            colUp = math.floor(colUp - ((colUp - colDown) / 2))
            print(c,colDown,colUp)
        if c == 'R':
            colDown = math.ceil(colUp - ((colUp - colDown)) / 2)
            print(c,colUp,colDown)
    row,col = rowDown,colDown
    return row * 8 + col

#simplify code


print(decodePass('FBFBBFFRLR'))

    