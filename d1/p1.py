# Day 1
# https://adventofcode.com/2021/day/1

increased = 0
with open('input.txt') as fp:
    first_row = fp.readline()
    prev = int(first_row)

    for row in fp:
        measure = int(row.strip())

        if measure > prev:
            increased += 1

        prev = measure

print(f"Increased {increased} times.")
