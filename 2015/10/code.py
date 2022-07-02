# Advent of code Year 2015 Day 10 solution
# Author = Szymon Kasprzycki
# Date = June 2022
from itertools import groupby

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.read()


def look_and_say(init_data):
    output = ""
    for key, group in groupby(init_data):
        output += str(len(list(group))) + str(key)
    return output


def part_one(data):
    for _ in range(40):
        data = look_and_say(data)
    return len(data)


def part_two(data):
    for _ in range(50):
        data = look_and_say(data)
    return len(data)


print(f"Part One: {str(part_one(input_data))}")
print(f"Part Two: {str(part_two(input_data))}")
