# Advent of code Year 2015 Day 9 solution
# Author = Szymon Kasprzycki
# Date = June 2022
import itertools
import sys


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input_data = input_file.read()


def get_unique_locations(initial_data: str):
    lines = initial_data.split('\n')
    words = [line.split(' ') for line in lines]
    locations = []
    for element in words:
        locations.extend((element[0], element[2]))
    return list(set(locations))


def get_travel_distances(initial_data: str):
    lines = initial_data.split('\n')
    words = [line.split(' ') for line in lines]
    distances = {}
    for item in words:
        distances.setdefault(item[0], dict())[item[2]] = int(item[4])
        distances.setdefault(item[2], dict())[item[0]] = int(item[4])
    return distances


def get_pairs(listed_data: list):
    return list(itertools.permutations(listed_data))


def main():
    unique_locations = get_unique_locations(input_data)
    travel_distances = get_travel_distances(input_data)
    travel_pairs = get_pairs(unique_locations)

    shortest = sys.maxsize
    longest = 0

    for items in travel_pairs:
        dist = sum(map(lambda x, y: travel_distances[x][y], items[:-1], items[1:]))
        shortest = min(shortest, dist)
        longest = max(longest, dist)

    print(f"Part One: {str(shortest)}")
    print(f"Part Two: {str(longest)}")

if __name__ == "__main__":
    main()