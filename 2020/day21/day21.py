import copy
import collections
with open("day21.txt") as f:
	lines = [line.rstrip().replace(")","").split(" (contains ") for line in f]
#print(lines)

def parse_input(lines):
	ingredient_list = []
	unique_ingredients = set()
	allergens_d = {}
	for line in lines:
		allergens_arr = line[1].split(", ")
		ingredients_arr = line[0].split(" ")
		unique_ingredients.update(ingredients_arr)
		ingredient_list.extend(ingredients_arr)
		# print(allergens_arr, ingredients_arr)
		for allergen in allergens_arr:

			if(allergen not in allergens_d):
				allergens_d[allergen] = set(ingredients_arr)
			else:
				allergens_d[allergen] = allergens_d[allergen] & set(ingredients_arr)
	return ingredient_list, unique_ingredients, allergens_d 

ingredient_list, unique_ingredients, allergens_d = parse_input(lines)
# print(allergens_d)

def map_allergenes(allergens_d):
	sure = set()
	while(len(allergens_d) < sum([(len(i)) for i in allergens_d.values()])):
		for key, value in allergens_d.items():
			if(len(value) == 1):
				sure.update(value)
			if(len(value) > 1):
				allergens_d[key] = value - sure
	print(allergens_d)
	return allergens_d

allergens_d = map_allergenes(allergens_d)

def part1(allergens_d, unique_ingredients, ingredient_list):
	result = 0
	allergen_free = unique_ingredients - set([list(i)[0] for i in allergens_d.values()])	
	for i in ingredient_list:
		if(i in allergen_free):
			result+=1
	print(result)

part1(allergens_d, unique_ingredients, ingredient_list)

def part2(allergens_d):
	result_str = ""
	od = collections.OrderedDict(sorted(allergens_d.items()))
	print(od)
	for v in od.values():
		result_str+= list(v)[0]+","
	print(result_str[:-1])

part2(allergens_d)