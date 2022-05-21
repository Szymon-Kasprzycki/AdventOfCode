# Advent of code Year 2015 Day 1 solution
# Author = Szymon Kasprzycki
# Date = May 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input_data = input_file.read()

# Part one
# Calculating the number of last floor that Santa would get to
floor = 0
for each in input_data:
    match each:
        case '(':
            floor += 1
        case ')':
            floor -= 1
        case _:
            pass

print(f"Part One: {str(floor)}")

# Part two
# Calculating the index of first instruction which makes Santa go to the basement
first_basement_index = 0
floor = 0
for index, each in enumerate(input_data):
    match each:
        case '(':
            floor += 1
        case ')':
            floor -= 1
        case _:
            pass
    if floor == -1:
        first_basement_index = index + 1
        break

print(f"Part Two: {str(first_basement_index)}")