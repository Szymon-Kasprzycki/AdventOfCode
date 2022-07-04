# Advent of code Year 2015 Day 17 solution
# Author = Szymon Kasprzycki
# Date = June 2022
from itertools import combinations

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.readlines()


def parse_input_data():
    containers = [int(x.strip()) for x in input_data]
    return containers


def get_containers_combinations(containers, target_capacity):
    possibilities = [p for number_of_bottles in range(len(containers)) for p in
                     combinations(containers, number_of_bottles) if sum(p) == target_capacity]
    return possibilities


def part_one():
    containers = parse_input_data()
    possibilities = get_containers_combinations(containers, 150)
    return len(possibilities)


def part_two():
    containers = parse_input_data()
    possibilities = get_containers_combinations(containers, 150)
    return len([p for p in possibilities if len(p) == len(min(possibilities, key=lambda x: len(x)))])


print(f"Part One: {str(part_one())}")
print(f"Part Two: {str(part_two())}")
