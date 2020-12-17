# Advent of code 2020 day 8 challenges

with open('Day8input.txt') as f:
    commands = [line.split(' ') for line in f.read().split("\n")]
commands.remove(commands[len(commands)-1]) #remove empty string at end of list

accumulator = 0
index = 0
history = []

while index >= 0:
    command = commands[index][0]
    value = int(commands[index][1]) #value of 'acc', 'jmp', or 'nop'
    if command == 'acc': 
        accumulator += value
        index += 1
    if command == 'nop':
        index += 1
    if command == 'jmp': 
        index += value
    if index in history:
        print('Last accumulator value: ', accumulator)
        break
    history.append(index)
    continue