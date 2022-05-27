# Advent of code Year 2015 Day 7 solution
# Author = Szymon Kasprzycki
# Date = May 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.readlines()

# Imports
import functools


# Part one
def _not_bitwise(*args):
    return ~args[0]


def _and_bitwise(*args):
    return args[0] & args[1]


def _or_bitwise(*args):
    return args[0] | args[1]


def _lshift_bitwise(*args):
    return args[0] << args[1]


def _rshift_bitwise(*args):
    return args[0] >> args[1]


def parse_instructions(data):
    wires_list = {}
    for line in data:
        operation, wire_name = line.split('->')
        wires_list[wire_name.strip()] = operation
    return wires_list


@functools.lru_cache()
def get_value(key):
    try:
        return int(key)
    except ValueError:
        pass

    wire_signal = wires[key].split(' ')
    if "NOT" in wire_signal:
        return _not_bitwise(get_value(wire_signal[1]))
    if "AND" in wire_signal:
        return _and_bitwise(get_value(wire_signal[0]), get_value(wire_signal[2]))
    elif "OR" in wire_signal:
        return _or_bitwise(get_value(wire_signal[0]), get_value(wire_signal[2]))
    elif "LSHIFT" in wire_signal:
        return _lshift_bitwise(get_value(wire_signal[0]), get_value(wire_signal[2]))
    elif "RSHIFT" in wire_signal:
        return _rshift_bitwise(get_value(wire_signal[0]), get_value(wire_signal[2]))
    else:
        return get_value(wire_signal[0])


wires = parse_instructions(input_data)
answer_one = get_value('a')
print(f"Part One: {str(answer_one)}")

wires['b'] = str(answer_one)
get_value.cache_clear()
answer_two = get_value('a')

print(f"Part Two: {answer_two}")
