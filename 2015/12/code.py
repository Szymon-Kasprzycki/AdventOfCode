# Advent of code Year 2015 Day 12 solution
# Author = Szymon Kasprzycki
# Date = June 2022
import json

with open((__file__.rstrip("code.py") + "input.json"), 'r') as input_file:
    input_data = json.load(input_file)


def part_one_recursive(data):
    recursive_sum = 0
    for each in data:
        try:
            recursive_sum += int(each)
        except (ValueError, TypeError):
            if isinstance(each, dict):
                recursive_sum += part_one_recursive(each.values())
            elif isinstance(each, list) or isinstance(each, tuple):
                recursive_sum += part_one_recursive(each)
            continue
    return recursive_sum


def part_two_recursive(data):
    recursive_sums = 0
    for each in data:
        if isinstance(each, int):
            recursive_sums += int(each)
        elif isinstance(each, dict) and 'red' not in each.values():
            print(each)
            recursive_sums += part_two_recursive(each.values())
        elif isinstance(each, list) or isinstance(each, tuple) and 'red' not in each:
            recursive_sums += part_two_recursive(each)
        continue
    return recursive_sums


print(f"Part One: {str(part_one_recursive(input_data.items()))}")
print(f"Part Two: {str(part_two_recursive(input_data.items()))}")
