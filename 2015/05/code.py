# Advent of code Year 2015 Day 5 solution
# Author = Szymon Kasprzycki
# Date = May 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = [line.strip() for line in input_file.readlines()]

# Part one
vowels = list('aeiou')
restricted_strings = ['ab', 'cd', 'pq', 'xy']
nice_strings = 0
for text_string in input_data:
    number_of_vowels = sum(text_string.count(vowel) for vowel in vowels)
    if number_of_vowels < 3:
        continue
    unique_letters = list(set(text_string))
    second_condition = set()
    for letter in unique_letters:
        if f'{letter}{letter}' in text_string:
            second_condition.add(True)
        else:
            second_condition.add(False)
    if not any(second_condition):
        continue
    third_condition = all(item not in text_string for item in restricted_strings)
    if not third_condition:
        continue
    nice_strings += 1

print(f"Part One: {str(nice_strings)}")

# Part two
nice_new_strings = 0
for text_string in input_data:
    first_new_condition = True
    for index in range(len(text_string) - 3):
        piece = text_string[index:index + 2]
        if piece in text_string[index + 2:]:
            first_new_condition = False
    if first_new_condition:
        continue
    second_new_condition = any(text_string[index] == text_string[index + 2] for index in range(len(text_string) - 2))
    if not second_new_condition:
        continue
    nice_new_strings += 1

print(f"Part Two: {str(nice_new_strings)}")
