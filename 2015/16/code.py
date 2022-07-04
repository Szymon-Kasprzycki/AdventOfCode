# Advent of code Year 2015 Day 16 solution
# Author = Szymon Kasprzycki
# Date = June 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.readlines()

check_data = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def read_aunts_data():
    aunts_data = {}
    for line in input_data:
        _, n, a, an, b, bn, c, cn = line.strip().replace(':', '').replace(',', '').split()
        aunts_data[n] = {
            a: int(an),
            b: int(bn),
            c: int(cn)
        }
    return aunts_data


def check(aunt_data: dict, check_data: dict, with_bugs: bool = False):
    passed = [False, False, False]
    x = 0
    for key, value in aunt_data.items():
        if (key not in ['cats', 'trees', 'pomeranians', 'goldfish'] and value == check_data[key] and with_bugs) or (
                value == check_data[key] and not with_bugs):
            passed[x] = True
        elif key in ['cats', 'trees'] and value > check_data[key]:
            passed[x] = True
        elif key in ['pomeranians', 'goldfish'] and value < check_data[key]:
            passed[x] = True
        x += 1
    return all(passed)


def part_one():
    aunts_data = read_aunts_data()
    for aunt_number, aunt_data in aunts_data.items():
        if check(aunt_data, check_data, False):
            return aunt_number


def part_two():
    aunts_data = read_aunts_data()
    for aunt_number, aunt_data in aunts_data.items():
        if check(aunt_data, check_data, True):
            return aunt_number


print(f"Part One: {str(part_one())}")
print(f"Part Two: {str(part_two())}")
