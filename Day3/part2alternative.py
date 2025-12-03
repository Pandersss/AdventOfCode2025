total = 0
data = [*open("input.txt")]

for number in data:
    finalNum = ''
    vnumArr = list(number.strip())
    for i in range(12, 0, -1):
        HighestNum = (vnumArr[0], '0')
        for i in range(len(vnumArr)-i):
            if vnumArr[i+1] > HighestNum[0]:
                HighestNum = ((vnumArr[i+1]), i+1)
        finalNum += HighestNum[0]
        vnumArr = vnumArr[int(HighestNum[1])+1:]
    total += int(finalNum)

print("Total: ",total)