# Advent of code Year 2015 Day 8 solution
# Author = Szymon Kasprzycki
# Date = May 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.read()


def parse_input(data: str):
    return [line for line in data.split('\n')]


def string_representation(text: str):
    representation = ''
    for char in text:
        match char:
            case '"':
                representation += "\\\""
            case '\\':
                representation += "\\\\"
            case _:
                representation += char
    return f'"{representation}"'


def memory_char_count(text: str):
    count = 0
    i = 1
    while i < len(text) - 1:
        if text[i] == "\\":
            i += 4 if text[i + 1] == "x" else 2
        else:
            i += 1
        count += 1
    return count


def literal_char_count(text: str):
    return len(text)


def part_one(data: list):
    memory_length = sum(memory_char_count(line) for line in data)
    literal_length = sum(literal_char_count(line) for line in data)
    return literal_length - memory_length


def part_two(data: list):
    encoded_length = sum(literal_char_count(string_representation(line)) for line in data)
    literal_length = sum(literal_char_count(line) for line in data)
    return encoded_length - literal_length


data_parsed = parse_input(input_data)

print(f"Part One: {str(part_one(data_parsed))}")
print(f"Part Two: {str(part_two(data_parsed))}")
