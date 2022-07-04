# Advent of code Year 2015 Day 15 solution
# Author = Szymon Kasprzycki
# Date = June 2022
from itertools import combinations_with_replacement

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input_data = input_file.readlines()


def get_ingredients():
    ingredients = {}
    for line in input_data:
        ingredient, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.replace(',', '').replace(':',
                                                                                                                   '').split()
        ingredients[ingredient] = {'capacity': int(capacity), 'durability': int(durability), 'flavor': int(flavor),
                                   'texture': int(texture), 'calories': int(calories)}
    return ingredients


def get_recipe_score(recipe, ingredients: dict, restricted_calories: bool = False):
    amount_of_ingerdients = {name: recipe.count(name) for name in ingredients.keys()}
    total_score = {'capacity': 0, 'durability': 0, 'flavor': 0, 'texture': 0, 'calories': 0}
    for ingredient in amount_of_ingerdients.keys():
        total_score['capacity'] += ingredients[ingredient]['capacity'] * amount_of_ingerdients[ingredient]
        total_score['durability'] += ingredients[ingredient]['durability'] * amount_of_ingerdients[ingredient]
        total_score['flavor'] += ingredients[ingredient]['flavor'] * amount_of_ingerdients[ingredient]
        total_score['texture'] += ingredients[ingredient]['texture'] * amount_of_ingerdients[ingredient]
        if restricted_calories:
            total_score['calories'] += ingredients[ingredient]['calories'] * amount_of_ingerdients[ingredient]
    if any([x <= 0 for x in [v for k, v in total_score.items() if k != 'calories']]) or (
            restricted_calories and total_score['calories'] != 500):
        return 0
    else:
        return total_score['capacity'] * total_score['durability'] * total_score['flavor'] * total_score['texture']


def get_recipe(ingredients: dict, amount_of_spoons: int, restricted_calories: bool = False):
    total_recipes_possibilities = combinations_with_replacement(ingredients.keys(), amount_of_spoons)
    for recipe in total_recipes_possibilities:
        score = get_recipe_score(recipe, ingredients, restricted_calories)
        if score > 0:
            yield score


def part_one():
    ingredients = get_ingredients()
    return max(get_recipe(ingredients, 100))


def part_two():
    ingredients = get_ingredients()
    return max(get_recipe(ingredients, 100, True))


print(f"Part One: {str(part_one())}")
print(f"Part Two: {str(part_two())}")
