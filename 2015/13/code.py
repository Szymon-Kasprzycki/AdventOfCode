# Advent of code Year 2015 Day 13 solution
# Author = Szymon Kasprzycki
# Date = June 2022
from itertools import permutations

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.readlines()


def get_guests(me: bool = False):
    guests = []
    for line in input_data:
        guest = line.split(" ")[0]
        if guest not in guests:
            guests.append(guest)
    if me:
        guests.append('Me')
    return guests


def get_dependencies():
    dependencies = {}
    for line in input_data:
        first_guest, _, dependency, amount, _, _, _, _, _, _, second_guest = line.split(" ")
        dependency = '+' if dependency == "gain" else '-'
        second_guest = second_guest[:-2]
        if first_guest not in dependencies:
            dependencies[first_guest] = []
        dependencies[first_guest].append({'person': second_guest, 'dependency': dependency, 'amount': int(amount)})
    return dependencies


def get_happiness(first_person, second_person, dependencies):
    happiness = 0
    for dependency in dependencies[first_person]:
        if dependency['person'] == second_person:
            happiness += dependency['amount'] if dependency['dependency'] == '+' else -dependency['amount']
    for dependency in dependencies[second_person]:
        if dependency['person'] == first_person:
            happiness += dependency['amount'] if dependency['dependency'] == '+' else -dependency['amount']
    return happiness


def get_highest_happiness(guests, dependencies):
    possibilities = list(permutations(guests, r=len(guests)))
    highest_happiness = 0
    for possibility in possibilities:
        happiness = 0
        for i in range(len(possibility) - 1):
            happiness += get_happiness(possibility[i], possibility[(i + 1) % len(possibility)], dependencies)
        happiness += get_happiness(possibility[-1], possibility[0], dependencies)
        if happiness > highest_happiness:
            highest_happiness = happiness
    return highest_happiness


def part_one():
    guests = get_guests()
    dependencies = get_dependencies()
    return get_highest_happiness(guests, dependencies)


def part_two():
    guests = get_guests(me=True)
    dependencies = get_dependencies()
    for guest in guests:
        if guest != 'Me':
            dependencies[guest].append({'person': 'Me', 'dependency': '+', 'amount': 0})
            dependencies['Me'] = [{'person': guest, 'dependency': '-', 'amount': 0}]
    return get_highest_happiness(guests, dependencies)


print(f"Part One: {str(part_one())}")
print(f"Part Two: {str(part_two())}")
