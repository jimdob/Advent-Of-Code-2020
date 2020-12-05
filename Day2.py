#Advent of code 2020 day 2 challenges

with open('Day2input.txt') as f:
    lines = f.read().splitlines() #read lines from txt into list
db = []
for line in lines: 
    line = line.split(':')              #split policy from password
    line = [i.strip() for i in line]    #clear space on ends
    line[0] = line[0].split(' ')        #split policy #'s from letter
    line[0][0] = line[0][0].split('-')  #split policy numbers
    line[0][0][0] = int(line[0][0][0])  #convert policy numbers to integers
    line[0][0][1] = int(line[0][0][1]) 
    db.append(line) #add separated values to list
# [[[4, 11], 'n'], 'ljgdnkgftmsvntnn'], example line in db after splitting

#PART 1

numValidP1 = 0
for element in db:
    letter = element[0][1]      #policy letter
    minLimit = element[0][0][0] #minimum occurences of letter
    maxLimit = element[0][0][1] #maximum occurences of letter
    password = element[1]       #password
    charCount = 0
    for char in password:       #count policy letter occurences in password
        if char == letter:      
            charCount += 1
    #determine if password meets policy criteria. Increment count if true
    if charCount >= minLimit and charCount <= maxLimit: numValidP1 += 1
print ('Part 1: ', numValidP1)

#PART 2

numValidP2 = 0
numInvalidP2 = 0
for element in db:
    letter = element[0][1]
    pos1 = (element[0][0][0]) - 1   #policy first position
    pos2 = (element[0][0][1]) - 1   #policy second position
    password = element[1]
    #if both positions have the policy letter, invalid password
    if password[pos1] == letter and password[pos2] == letter: numInvalidP2 += 1
    #if only one of the positions has the policy letter, valid password
    elif password[pos1] == letter or password[pos2] == letter: numValidP2 +=1
print('Part 2: ', numValidP2)

    