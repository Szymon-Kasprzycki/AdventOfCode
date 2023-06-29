# Advent of code Year 2015 Day 21 solution
# Author = Szymon Kasprzycki
# Date = June 2023
import itertools
import sys
import copy

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.read()
    boss_data = {str(line.split(': ')[0]): int(line.split(': ')[1]) for line in input_data.splitlines()}
    player_data = {'Hit Points': 100, 'Damage': 0, 'Armor': 0}

equipment = {
    'armor': {
        'leather': {'cost': 13, 'damage': 0, 'armor': 1},
        'chainmail': {'cost': 31, 'damage': 0, 'armor': 2},
        'splintmail': {'cost': 53, 'damage': 0, 'armor': 3},
        'bandedmail': {'cost': 75, 'damage': 0, 'armor': 4},
        'platemail': {'cost': 102, 'damage': 0, 'armor': 5}
    },
    'weapon': {
        'dagger': {'cost': 8, 'damage': 4, 'armor': 0},
        'shortsword': {'cost': 10, 'damage': 5, 'armor': 0},
        'warhammer': {'cost': 25, 'damage': 6, 'armor': 0},
        'longsword': {'cost': 40, 'damage': 7, 'armor': 0},
        'greataxe': {'cost': 74, 'damage': 8, 'armor': 0},
    },
    'rings': {
        'damage+1': {'cost': 25, 'damage': 1, 'armor': 0},
        'damage+2': {'cost': 50, 'damage': 2, 'armor': 0},
        'damage+3': {'cost': 100, 'damage': 3, 'armor': 0},
        'defense+1': {'cost': 20, 'damage': 0, 'armor': 1},
        'defense+2': {'cost': 40, 'damage': 0, 'armor': 2},
        'defense+3': {'cost': 80, 'damage': 0, 'armor': 3},
    }
}

rings = tuple(list(equipment['rings'].values()) + [{}])
armors = tuple(list(equipment['armor'].values()) + [{}])
weapons = equipment['weapon'].values()


def did_player_win(player):
    boss = copy.deepcopy(boss_data)
    attacker_c = itertools.cycle([player, boss])
    defender_c = itertools.cycle([boss, player])
    while True:
        attacker = next(attacker_c)
        defender = next(defender_c)
        defender['Hit Points'] -= max(attacker['Damage'] - defender['Armor'], 1)
        if defender['Hit Points'] <= 0:
            return defender == boss


def part_one():
    min_cost = sys.maxsize
    for armor in armors:
        for weapon in weapons:
            for combination in itertools.combinations(rings, 2):
                player = copy.deepcopy(player_data)
                cost = 0
                for item in [armor, weapon, *combination]:
                    if not item:
                        continue
                    player['Damage'] += item['damage']
                    player['Armor'] += item['armor']
                    cost += item['cost']

                if did_player_win(player):
                    min_cost = min(min_cost, cost)

    return min_cost


def part_two():
    max_cost = -sys.maxsize
    for armor in armors:
        for weapon in weapons:
            for combination in itertools.combinations(rings, 2):
                player = copy.deepcopy(player_data)
                cost = 0
                for item in [armor, weapon, *combination]:
                    if not item:
                        continue
                    player['Damage'] += item['damage']
                    player['Armor'] += item['armor']
                    cost += item['cost']

                if not did_player_win(player):
                    max_cost = max(max_cost, cost)

    return max_cost


print(f"Part One: {str(part_one())}")
print(f"Part Two: {str(part_two())}")
