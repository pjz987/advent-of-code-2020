from parse_input import parse

raw_input = parse('41input.txt')

def check_ingredients_len(allergens_dict):
  for ingredients in allergens_dict.values():
    if len(ingredients) > 1:
      return True
  return False

def remove_ingredient_from_other_allergen_ingredient_lists(allergen, ingredient, allergens_dict):
  for allergen_key in allergens_dict.keys():
    if allergen_key != allergen and ingredient in allergens_dict[allergen_key]:
      allergens_dict[allergen_key].remove(ingredient)
  return allergens_dict

foods = []
for line in raw_input:
  ingredients = line.split(' (contains ')[0]
  allergens = line.split(' (contains ')[1].strip(')')
  ingredients = ingredients.split()
  allergens = allergens.split(', ')
  food_dict = {
    'ingredients': ingredients,
    'allergens': allergens
  }
  foods.append(food_dict)

ingredients_list = []
allergens_list = []
for food in foods:
  ingredients_list.extend(food['ingredients'])
  allergens_list.extend(food['allergens'])

ingredients_set = set(ingredients_list)
allergens_set = set(allergens_list)

# print(ingredients)
# print(allergens)

allergens_dict = {}

for allergen in allergens_set:
  first = True
  for food in foods:
    if allergen in food['allergens']:
      if first:
        ingredients_set = set(food['ingredients'])
        first = False
      else:
        ingredients_set = ingredients_set.intersection(set(food['ingredients']))
  allergens_dict[allergen] = list(ingredients_set)

while check_ingredients_len(allergens_dict):
  for allergen, ingredients in allergens_dict.items():
    if len(ingredients) == 1:
      allergens_dict = remove_ingredient_from_other_allergen_ingredient_lists(allergen, ingredients[0], allergens_dict)

ingredients_set = set(ingredients_list)

allergens_set_verified = set([value[0] for value in allergens_dict.values()])
allergen_free_ingredients = ingredients_set.difference(allergens_set_verified)
print(allergen_free_ingredients)
count = 0
for line in raw_input:
  for ingredient in allergen_free_ingredients:
    if ingredient in line:
      print(ingredient, line)
      count += 1
print(count)