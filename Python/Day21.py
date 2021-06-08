from functools import reduce

inputString = open("Day21Input.txt", "r").read().splitlines()

def processIngredients():
    allergensSets, allIngredients, uniqueIngredients = {}, [], {}
    for line in inputString:
        ingredients, allergens = line.split(" (contains ")
        ingredients = ingredients.split(" ")
        allIngredients.extend(ingredients)
        for allergen in allergens[:-1].split(", "):
            if allergen in allergensSets.keys():
                allergensSets[allergen] &= set(ingredients)
            else:
                allergensSets[allergen] = set(ingredients)
    safeIngredients = set(allIngredients) - reduce(lambda a, b: a.union(b), allergensSets.values())
    print(sum([allIngredients.count(ingredient) for ingredient in safeIngredients]))
    while max([len(ingredients) for ingredients in allergensSets.values()]) > 0:
        for allergens, ingredients in allergensSets.items():
            if len(ingredients) == 1: uniqueIngredients[allergens] = ingredients.pop()
        for allergen in allergensSets:
            allergensSets[allergen] -= set(uniqueIngredients.values())
    print(",".join([ingredient for (allergen, ingredient) in sorted(uniqueIngredients.items())]))

processIngredients()
