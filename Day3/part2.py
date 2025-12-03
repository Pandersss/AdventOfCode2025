# Advent of code 2025 Day 3.
# This year there will be absolutely no use of any kind of AI! I would rather give up.
# Part 2

total = 0
data = [*open("input.txt")]

def findFirstHighestNum(num, buff):
    numArr = list(num)
    HighestNum = (numArr[0], '0')
    for i in range(len(numArr)-buff):
        if numArr[i+1] > HighestNum[0]:
            HighestNum = ((numArr[i+1]), i+1)
    return HighestNum

for number in data:
    finalNum = ''
    vnumber = number.strip()
    for i in range(12, 0, -1):
        HighestNum = findFirstHighestNum(vnumber, i)
        finalNum += HighestNum[0]
        vnumber = vnumber[int(HighestNum[1])+1:]
    total += int(finalNum)

print("Total: ",total)