# Advent of code 2025 Day 3.
# This year there will be absolutely no use of any kind of AI! I would rather give up.
# Part 1

data = []
FirstNum = []
SecondNum = []
total = 0

file = open("input.txt","r")
for line in file:
    data.append(line.strip())

def findFirstHighestNum(num, buff):
    numArr = list(num)
    HighestNum = [numArr[0], '0']
    for i in range(len(numArr)-buff):
        if numArr[i+1] > HighestNum[0]:
            HighestNum = [numArr[i+1], i+1]
    return HighestNum

def findSecondHighestNum(num, First):
    position = int(First[1])
    cutNum = num[position+1:]
    return findFirstHighestNum(cutNum, 1)

for number in data:
    FirstNum = findFirstHighestNum(number, 2)
    SecondNum = findSecondHighestNum(number, FirstNum)
    voltagePer = FirstNum[0] + SecondNum[0]
    total += int(voltagePer)

print("Total: ",total)