
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
            
allergen_ingredients = set()
for a in allergen_dict.values():
    allergen_ingredients |= a

safe_ingredients = set(ingredients_list) - allergen_ingredients

ans=0
for j in ingredients_list:
        if j in safe_ingredients:
            ans += 1

print(ans)

