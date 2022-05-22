# Advent of code Year 2015 Day 6 solution
# Author = Szymon Kasprzycki
# Date = May 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input_data = [[y.strip() for y in x.split(' ')] for x in input_file.readlines()]

# Imports
import numpy as np

# Part one
lights_grid = np.zeros(shape=(1000, 1000), dtype=np.int8)
for instruction in input_data:
    end_coordinates = [int(x) for x in instruction[-1].split(',')]
    start_coordinates = [int(x) for x in instruction[-3].split(',')]
    if 'on' in instruction:
        lights_grid[slice(start_coordinates[0], end_coordinates[0]+1), slice(start_coordinates[1], end_coordinates[1]+1)] = 1
    elif 'off' in instruction:
        lights_grid[slice(start_coordinates[0], end_coordinates[0]+1), slice(start_coordinates[1], end_coordinates[1]+1)] = 0
    elif 'toggle' in instruction:
        lights_grid[slice(start_coordinates[0], end_coordinates[0]+1), slice(start_coordinates[1], end_coordinates[1]+1)] ^= 1

answer_one = np.count_nonzero(lights_grid == 1)
print(f"Part One: {str(answer_one)}")

# Part two
lights_grid = np.zeros(shape=(1000, 1000), dtype=np.int8)
for instruction in input_data:
    end_coordinates = [int(x) for x in instruction[-1].split(',')]
    start_coordinates = [int(x) for x in instruction[-3].split(',')]
    if 'on' in instruction:
        lights_grid[slice(start_coordinates[0], end_coordinates[0] + 1), slice(start_coordinates[1], end_coordinates[1] + 1)] += 1
    elif 'off' in instruction:
        lights_grid[slice(start_coordinates[0], end_coordinates[0] + 1), slice(start_coordinates[1], end_coordinates[1] + 1)] -= 1
    elif 'toggle' in instruction:
        lights_grid[slice(start_coordinates[0], end_coordinates[0] + 1), slice(start_coordinates[1], end_coordinates[1] + 1)] += 2
    lights_grid[lights_grid < 0] = 0

answer_two = np.sum(lights_grid)
print(f"Part Two: {str(answer_two)}")