# Advent of code Year 2015 Day 11 solution
# Author = Szymon Kasprzycki
# Date = May 2022
import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input_data = input_file.read()


# Get letter ASCII code
def get_code_letter(letter):
    return ord(letter)


# Get the letter from ASCII code
def get_letter_from_code(code):
    return chr(code)


# Get the next letter in the alphabet
def get_next_letter(letter):
    if letter == 'z':
        return 'a'
    return get_letter_from_code(get_code_letter(letter) + 1)


def check_pass(password):
    if any(letter in password for letter in ['i', 'o', 'l']) or \
           (len(re.findall(r'([a-z])\1', password)) < 2) or \
           (len([1 for x, y, z in zip(password, password[1:], password[2:])
                   if get_code_letter(z)-get_code_letter(y) == 1 and get_code_letter(y)-get_code_letter(x) == 1]) == 0):
        return False
    return True


def gen_pass(start_pass):
    start_pass = re.sub(r'([a-y])(z*)$', lambda x: chr(ord(x.group(1))+1) + len(x.group(2))*"a", start_pass)
    return start_pass


def part_one():
    password = input_data
    while True:
        password = gen_pass(password)
        if check_pass(password):
            break
    return password


def part_two():
    password = input_data
    counter = 0
    while True:
        password = gen_pass(password)
        if check_pass(password):
            counter += 1
            if counter == 2:
                break
    return password


print(f"Part One: {str(part_one())}")

print(f"Part Two: {str(part_two())}")