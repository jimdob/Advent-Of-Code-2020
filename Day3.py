# Advent of code 2020 day 3 challenges

with open('Day3input.txt') as f:
    lines = f.read().splitlines() #read lines from txt into list

#PART 1
def rideToboggan (right, down):
    row, pos = 0, 1
    numTrees = 0
    width = len(lines[0])
    while row < (len(lines) - 1):
        row += down #move down
        pos += right #move right
        if pos > width: #resets position to the start of the row if row limit exceeded
            pos = pos % width
        if lines[row][pos-1] == '#': #if on a tree (#), increment tree counter
            numTrees += 1
    return numTrees

print('Part 1: ',rideToboggan(3,1))

#PART 2
totalTrees = (rideToboggan(1,1) * 
            rideToboggan(3,1) * 
            rideToboggan(5,1) *
            rideToboggan(7,1) *
            rideToboggan(1,2))
print('Part 2: ',totalTrees)