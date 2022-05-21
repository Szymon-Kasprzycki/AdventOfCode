# Advent of code Year 2015 Day 3 solution
# Author = Szymon Kasprzycki
# Date = May 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip()

# Imports
import numpy as np
import math


# Functions
def change_coordinates(direction: str, coordinates: list):
    """
    It takes a move direction and a set of coordinates, and returns a new set of coordinates after the move by 1 step

    :param direction: The direction the Santa is going
    :type direction: str
    :param coordinates: a list of the current coordinates of the santa
    :type coordinates: list
    :return: The coordinates of the house that Santa visited.
    """
    match direction:
        case '^':
            coordinates[1] += 1
        case 'v':
            coordinates[1] -= 1
        case '<':
            coordinates[0] -= 1
        case '>':
            coordinates[0] += 1
        case _:
            pass
    return coordinates


# Part one
# Creating a map of the houses that Santa visits and counting amount of presents given to each house
dimensions = math.floor(len(input_data) / 4)
santa_map = np.zeros((dimensions, dimensions), dtype=np.int8)
position_coordinates = [int(dimensions / 4), int(dimensions / 4)]
for instruction in input_data:
    position_coordinates = change_coordinates(instruction, position_coordinates)
    santa_map[position_coordinates[0], position_coordinates[1]] += 1

answer_1 = np.sum(santa_map >= 1)
print(f"Part One: {str(answer_1)}")

# Part two
dimensions = math.floor(len(input_data) / 8)
world_map = np.zeros((dimensions, dimensions), dtype=np.int8)
santa_coordinates, robot_coordinates = [int(dimensions / 8), int(dimensions / 8)], [int(dimensions / 8),
                                                                                    int(dimensions / 8)]
for index, instruction in enumerate(input_data):
    if index % 2 == 0:
        santa_coordinates = change_coordinates(instruction, santa_coordinates)
        world_map[santa_coordinates[0], santa_coordinates[1]] += 1
    else:
        robot_coordinates = change_coordinates(instruction, robot_coordinates)
        world_map[robot_coordinates[0], robot_coordinates[1]] += 1

answer_2 = np.sum(world_map >= 1)
print(f"Part Two: {str(answer_2)}")
