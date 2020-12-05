# Advent of code 2020 day 4 challenges
import re

with open('Day4input.txt') as f:
    lines = f.read().split("\n\n") #read lines from txt into list

totalPassports = len(lines)
validPassportsP1 = 0
validPassportsP2 = 0
validCredentials = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #removed 'cid'

db = []
d = {}

# Turn each passport into dictionary and add passports with all
#   valid credential categories to a list ("db")
for line in lines:
    line = re.split(" |\n", line)  
    line = list(filter(None, line))
    line = [j.split(":") for j in line]
    for k in line:
        (key,val) = k[0],k[1]
        d[(key)] = val
    if all(keys in d for keys in validCredentials):
        validPassportsP1 += 1
        db.append(d)
    d = {}

#Clean passport data for validating
validECL = ['amb','blu','brn','gry','grn','hzl','oth']

for passport in db:
    validFields = 0
    
    if 1920 <= int(passport['byr']) <= 2002: validFields += 1
    if 2010 <= int(passport['iyr']) <= 2020: validFields += 1
    if 2020 <= int(passport['eyr']) <= 2030: validFields += 1
    if passport['hgt'].endswith('cm'):
        if 150 <= int(passport['hgt'].replace('cm','')) <= 193: validFields += 1
    if passport['hgt'].endswith('in'):
        if 59 <= int(passport['hgt'].replace('in','')) <= 76: validFields += 1
    if passport['hcl'].startswith('#') and len(passport['hcl']) == 7:
        pattern = re.compile(r'[^a-f0-9]')
        if not re.search(pattern, passport['hcl'].replace('#','')):
            validFields += 1
    if any(ecl in passport['ecl'] for ecl in validECL): validFields += 1
    if len(passport['pid']) == 9 and passport['pid'].isdigit(): validFields += 1
    
    if validFields >= 7: validPassportsP2 += 1

print('Valid passports p1: ',validPassportsP1)
print('Valid passports p2: ',validPassportsP2)
print('Total passports: ',totalPassports)
