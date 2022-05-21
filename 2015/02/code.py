# Advent of code Year 2015 Day 2 solution
# Author = Szymon Kasprzycki
# Date = May 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = [[int(dimension.strip()) for dimension in box.split('x')] for box in input_file.readlines()]

# Part one
# Calculating the amount of paper needed to wrap the present.
amount_of_paper = 0
for box in input_data:
    side_a = box[0] * box[1]
    side_b = box[1] * box[2]
    side_c = box[0] * box[2]
    amount_of_paper += 2 * side_a + 2 * side_b + 2 * side_c + min(side_a, side_b, side_c)

print(f"Part One: {str(amount_of_paper)}")

# Part two
# Calculating the length of ribbon needed to wrap the present.
length_of_ribbon = 0
for box in input_data:
    box_dimensions = sorted(box)
    volume_of_present = box[0] * box[1] * box[2]
    shortest_around_distance = 2 * box_dimensions[0] + 2 * box_dimensions[1]
    length_of_ribbon += (volume_of_present + shortest_around_distance)

print(f"Part Two: {str(length_of_ribbon)}")
