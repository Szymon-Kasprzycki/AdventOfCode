# Advent of code Year 2015 Day 4 solution
# Author = Szymon Kasprzycki
# Date = May 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.read()

# Imports
import hashlib
import itertools


# Functions
def find_lowest_number(secret_key: str, amount_of_zeros: int):
    """
    It takes a secret key and an amount of zeros, and returns the lowest number that, when hashed with the secret key,
    produces a hash that starts with the given amount of zeros

    :param secret_key: The secret key that is used to generate the hash
    :type secret_key: str
    :param amount_of_zeros: The amount of zeros that the hash must start with
    :type amount_of_zeros: int
    :return: The lowest number that when hashed with the secret key, returns a hash that starts with the amount of zeros
    """
    for iterator in itertools.count(1):
        md5_hashed = hashlib.md5(f'{secret_key}{iterator}'.encode()).hexdigest()
        if md5_hashed.startswith('0' * amount_of_zeros):
            return iterator


# Part One
answer_one = find_lowest_number(input_data, 5)
print(f"Part One: {str(answer_one)}")

# Part Two
answer_two = find_lowest_number(input_data, 6)
print(f"Part Two: {str(answer_two)}")
