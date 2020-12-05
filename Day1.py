#Advent of code 2020 day 1 challenges

with open("Day1input.txt") as f:
    data = list(map(int, f.readlines()))

targetSum = 2020
print('Target sum: ',targetSum)
#PART 1

for x in data:
    for y in data:
        if x + y == targetSum:
            p1x,p1y = x,y
print('Part 1')
print('{} + {} is {}'.format(p1x,p1y,p1x+p1y))
print('{} * {} is {}'.format(p1x,p1y,p1x*p1y))

#PART 2

for x in data:
    for y in data:
        for z in data:
            if x + y + z == targetSum:
                p2x,p2y,p2z = x,y,z

print('Part 2')
print('{} + {} + {} is {}'.format(p2x,p2y,p2z,p2x+p2y+p2z))
print('{} * {} * {} is {}'.format(p2x,p2y,p2z,p2x*p2y*p2z))