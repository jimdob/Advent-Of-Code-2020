# Advent of code 2020 day 6 challenges

import re

#split into list of groups, containing a list of answers in each group
with open('Day6input.txt') as f:
    groups = [line.split('\n') for line in [group.strip() for group in f.read().split("\n\n")]]

#PART 1
totalCount = 0
for group in groups:
    totalCount += len(set(''.join(group))) #counts unique answers in each group
print('Part 1: ',totalCount)

# PART 2
countUnanimousAnswers = 0
for group in groups:
    numPeople = len(group)  # number of people in group
    answers = ''.join(group) # single string of every person's answers in group
    unique = set(answers)   # set of unique answers in the group
    # iterate set of group answers, count occurences in "joined" 
    # if occurences equals the number of people, everyone answered yes
    for char in unique:
        if (len(re.findall(char, answers))) == numPeople:
            countUnanimousAnswers += 1
print('Part 2: ',countUnanimousAnswers)
