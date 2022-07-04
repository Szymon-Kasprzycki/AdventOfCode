# Advent of code Year 2015 Day 14 solution
# Author = Szymon Kasprzycki
# Date = June 2022

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = [line.split(' ') for line in input_file.readlines()]


def get_reindeer_data():
    return {f'{line[0]}': {'velocity': int(line[3]), 'time': int(line[6]), 'rest': int(line[13])} for line in
            input_data}


def get_reindeer_state(reindeer_data: dict, time: int):
    actual_riding_time = time % (reindeer_data['time'] + reindeer_data['rest'])
    actual_riding_time = reindeer_data['time'] if actual_riding_time > reindeer_data['time'] else actual_riding_time
    times_elapsed = time // (reindeer_data['time'] + reindeer_data['rest'])
    return {'distance': times_elapsed * reindeer_data['time'] * reindeer_data['velocity'] + actual_riding_time *
                        reindeer_data['velocity'], 'times_elapsed': times_elapsed, 'actual_time': actual_riding_time}


def part_one(time: int):
    reindeer_data = get_reindeer_data()
    reindeer_list = {name: get_reindeer_state(data, time) for name, data in reindeer_data.items()}
    return max(reindeer_list.values(), key=lambda x: x['distance'])['distance']


def part_two(time: int):
    reindeer_data = get_reindeer_data()
    for name, data in reindeer_data.items():
        reindeer_data[name]['score'] = 0
    for i in range(1, time):
        reindeer_list = {name: get_reindeer_state(data, i) for name, data in reindeer_data.items()}
        winning = max(reindeer_list.values(), key=lambda x: x['distance'])
        key = [k for k, v in reindeer_list.items() if v == winning]
        reindeer_data[key[0]]['score'] += 1
    return max(reindeer_data.values(), key=lambda x: x['score'])['score']


print(f"Part One: {str(part_one(2503))}")

print(f"Part Two: {str(part_two(2503))}")
