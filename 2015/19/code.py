# Advent of code Year 2015 Day 19 solution
# Author = Szymon Kasprzycki
# Date = May 2022
from random import shuffle

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.read()


def process_input(input_data):
    data = []
    for line in input_data.split("\n"):
        info = line.split(" ")
        data.append((info[0], info[-1]))
    molecule = data[-1][0]
    return data[:-2], molecule


def generate_molecules(data, molecule):
    molecules = set()
    for i, j in data:
        if i in molecule:
            for c in range(len(molecule)):
                if molecule[c:c + len(i)] == i:
                    molecules.add(molecule[:c] + j + molecule[c + len(i):])
    return len(molecules)


def part_one():
    data, molecule = process_input(input_data)
    return generate_molecules(data, molecule)


def part_two():
    data, molecule = process_input(input_data)
    target = molecule
    part2 = 0

    while target != 'e':
        tmp = target
        for a, b in data:
            if b not in target:
                continue

            target = target.replace(b, a, 1)
            part2 += 1

        if tmp == target:
            target = molecule
            part2 = 0
            shuffle(data)
    return part2


print(f"Part One: {str(part_one())}")
print(f"Part Two: {str(part_two())}")
