# Day 1
# https://adventofcode.com/2021/day/1

with open('input.txt') as fp:
    rows = list(map(int, fp.readlines()))

increased = 0
prev = sum(rows[:3])

for i in range(1, len(rows) - 2):
    measure = sum(rows[i:i+3])
    print(measure)
    if measure > prev:
        increased += 1

    prev = measure

print(f"Increased {increased} times.")
