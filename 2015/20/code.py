# Advent of code Year 2015 Day 20 solution
# Author = Szymon Kasprzycki
# Date = May 2022
import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = int(input_file.read().strip())


def part_one():
    houses = np.zeros(1000000)
    for elf in range(1, 1000000):
        houses[elf::elf] += 10 * elf
    return np.nonzero(houses >= input_data)[0][0]


def part_two():
    houses = np.zeros(1000000)
    for elf in range(1, 1000000):
        houses[elf:(elf + 1) * 50:elf] += 11 * elf
    return np.nonzero(houses >= input_data)[0][0]


print("Part one:", part_one())
print("Part two:", part_two())
