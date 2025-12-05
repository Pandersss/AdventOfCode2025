# Advent of code 2025 Day 4.
# This year there will be absolutely no use of any kind of AI! I would rather give up.
# Part 1
# This code is horrible but could not bother with numpy, or fixing it

total = 0
arr = []
tmparr = []

data = [*open("input.txt")]
for line in range(len(data)):
    for c in data[line].strip():
        tmparr.append(c)
    arr.append(tmparr)
    tmparr = []

for x, row in enumerate(arr):
    for y, roll in enumerate(row):
        count = 0
        if roll == '@':
            if x != 0 and y != 0:
                if arr[x-1][y-1] == '@':
                    count += 1
            if x != 0:
                if arr[x-1][y] == '@':
                    count += 1
            if x != 0 and y != len(row)-1:
                if arr[x-1][y+1] == '@':
                    count += 1
            if y != 0:
                if arr[x][y-1] == '@':
                    count += 1
            if y != len(row)-1:
                if arr[x][y+1] == '@':
                    count += 1
            if x != len(arr)-1 and y != 0:
                if arr[x+1][y-1] == '@':
                    count += 1
            if x != len(arr)-1:
                if arr[x+1][y] == '@':
                    count += 1
            if x != len(arr)-1 and y != len(row)-1:
                if arr[x+1][y+1] == '@':
                    count += 1
            if count < 4:
                total += 1

print("Total found:", total)