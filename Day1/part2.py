# Advent of code 2025 Day 1.
# This year there will be absolutely no use of any kind of AI! I would rather give up.
# Part 2

moves = []
dial = 50
zeroamount = 0

file = open("input.txt","r")
for line in file:
    moves.append(line.strip())

def move_left_once():
    global dial
    check_zero()
    if dial == 0:
        dial = 99
    else:
        dial = dial - 1

def move_right_once():
    global dial
    check_zero()
    if dial == 99:
        dial = 0
    else:
        dial = dial + 1

def check_zero():
    global dial, zeroamount
    if dial == 0:
        zeroamount = zeroamount + 1

for line in moves:
    if line[:1] == "L":
        for i in range(int(line[1:])):
            move_left_once()
    if line[:1] == "R":
        for i in range(int(line[1:])):
            move_right_once()

print("Final amount ot zeroes: ", zeroamount)