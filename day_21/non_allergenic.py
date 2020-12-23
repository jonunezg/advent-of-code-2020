from os import path

with open(path.dirname(__file__) + '/input.txt') as f:
    print('Count the number of times ingredients that cannot have allergens appear')
    recipes = [(entry[0].strip().split(' '), entry[1].strip().split(' ')) for entry in [line.strip('\n').replace('(', '').replace(')', '').replace(',', '').split('contains') for line in f.readlines()]]
    candidates = {}
    for ingredients, allergens in recipes:
        for allergen in allergens:
            candidates[allergen] = [ingredient for ingredient in candidates.get(allergen, ingredients) if ingredient in ingredients]

    all_candidates = {}
    for ingredients in candidates.values():
        for ingredient in ingredients:
            all_candidates[ingredient] = True
    print('Number of ingredient mentions with no possible allergen: {0}'.format(sum([sum([1 for ingredient in ingredients if ingredient not in all_candidates]) for ingredients, _ in recipes])))

    matched = {}
    while True: # Reduce found combinations of ingredient-allergen and try to find new ones
        current = len(matched)
        for allergen, ingredients in candidates.items():
            candidates[allergen] = [ingredient for ingredient in ingredients if ingredient not in matched] # Removed known ingredients from which the allergen is known
            if len(candidates[allergen]) == 1:
                matched[candidates[allergen][0]] = allergen
        if len(matched) == current: # No other ingredient-allergen unique combination found, finished or not enough data to decide on the rest
            break
    print('Ingredients sorted by their allergen (alphabetical order):', ','.join([ingredient for ingredient, _ in sorted(matched.items(), key = lambda x : x[1])]))
