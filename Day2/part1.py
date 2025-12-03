# Advent of code 2025 Day 2.
# This year there will be absolutely no use of any kind of AI! I would rather give up.
# Part 1

total = 0

file = open("input.txt","r")
for lines in file:
    idRanges = lines.split(',')

def isInvalid(checknum):
    global total
    checknum = str(checknum)
    if len(checknum) % 2 == 0:
        half = int(len(checknum)/2)
        if checknum[:half] == checknum[half:]:
            total = total + int(checknum)

for idRange in idRanges:
    idRange2 = idRange.split('-')
    startNum = int(idRange2[0])
    iterations = int(idRange2[1]) - int(idRange2[0])
    for i in range(iterations+1):
        isInvalid(startNum)
        startNum += 1

print("Total:", total)