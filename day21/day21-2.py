
allergen_dict={}
ingredients_list=[]
with open('input.txt') as f:
    for line in f:
        ingredients, allergens = line.strip().split(' (contains ')
        ingredients = ingredients.split()
        allergens = allergens.replace(')', '').split(', ')
        ingredients_list.extend(ingredients)
        for a in allergens:
            if a in allergen_dict:
                allergen_dict[a] &= set(ingredients)
            else:
                allergen_dict[a] = set(ingredients)

dangerous_ingredients = {i: None for i in allergen_dict.keys()}
empty = set(dangerous_ingredients.values())

while None in dangerous_ingredients.values():
    for a, i_set in allergen_dict.items():
        t = allergen_dict[a]

        for i in dangerous_ingredients.values():
            if i in i_set:
                allergen_dict[a] -= {i}

        if len(t) == 1:
            dangerous_ingredients[a] = list(t)[0]

print(','.join([dangerous_ingredients[a] for a in sorted(dangerous_ingredients.keys())]))


