# Advent of code 2025 Day 2.
# This year there will be absolutely no use of any kind of AI! I would rather give up.
# Part 2

from itertools import groupby

total = 0

file = open("input.txt","r")
for lines in file:
    idRanges = lines.split(',')

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def isInvalid(checknum):
    global total
    checknum = str(checknum)
    half = int(len(checknum)/2)
    for i in range(half):
        if len(checknum) % half == 0:
            values = map(''.join, zip(*[iter(checknum)]*half))
            if all_equal(values) == True:
                total += int(checknum)
                break
        half -= 1

for idRange in idRanges:
    idRange2 = idRange.split('-')
    startNum = int(idRange2[0])
    iterations = int(idRange2[1]) - int(idRange2[0])
    for i in range(iterations+1):
        isInvalid(startNum)
        startNum += 1

print("Total:", total)