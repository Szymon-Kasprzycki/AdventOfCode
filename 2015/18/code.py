# Advent of code Year 2015 Day 18 solution
# Author = Szymon Kasprzycki
# Date = June 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.readlines()


def read_init_data():
    data = [[1 if char == '#' else 0 for char in line] for line in input_data]
    return [line[:-1] if len(line) == 101 else line for line in data]


def process_data(data, blocked_corners: bool = False):
    new_data = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    if blocked_corners:
        new_data[0][0] = 1
        new_data[0][-1] = 1
        new_data[-1][0] = 1
        new_data[-1][-1] = 1
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_data[i][j] = get_new_value(data, i, j, blocked_corners)
    return new_data


def get_new_value(data, i, j, blocked_corners: bool = False):
    neighbours = get_neighbours(data, i, j)
    if blocked_corners:
        if i == 0 and j == 0 or \
                i == 0 and j == len(data[0]) - 1 or \
                i == len(data) - 1 and j == 0 or \
                i == len(data) - 1 and j == len(data[0]) - 1:
            return 1
    if neighbours == 3:
        return 1
    elif neighbours == 2:
        return data[i][j]
    else:
        return 0


def get_neighbours(data, i, j):
    neighbours = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if i + x < 0 or i + x >= len(data):
                continue
            if j + y < 0 or j + y >= len(data[0]):
                continue
            neighbours += data[i + x][j + y]
    return neighbours


def part_one():
    data = read_init_data()
    for _ in range(100):
        data = process_data(data)
    return sum([sum(line) for line in data])


def part_two():
    data = read_init_data()
    data[0][0] = 1
    data[0][-1] = 1
    data[-1][0] = 1
    data[-1][-1] = 1
    for _ in range(100):
        data = process_data(data, True)
    return sum([sum(line) for line in data])


print(f"Part One: {str(part_one())}")
print(f"Part Two: {str(part_two())}")
