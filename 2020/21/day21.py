def read_data(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")
    foods = [set(food.split(" (contains ")[0].split(" ")) for food in data]
    allergens = [food.split(" (contains ")[1][:-1].split(", ") for food in data]
    return foods, allergens

tfoods, tallergens = read_data("testa.txt")
foods, allergens = read_data("day21.txt")

# PART 1
def find_allergens(foods, allergens):
    ingredients = {}
    for i in range(len(foods)):
        for allergen in allergens[i]:
            food = foods[i]
            if allergen not in ingredients:
                ingredients[allergen] = set(food)
            else:
                ingredients[allergen].intersection_update(food)
    return ingredients

def count_bad(ingredients, foods):
    good = {ingr for alrg in ingredients.values() for ingr in alrg}
    cnt = 0
    for recipe in foods:
        for ingr in recipe:
            if ingr not in good:
                cnt += 1
    return cnt

def part1(foods, allergens):
    ingredients = find_allergens(foods, allergens)
    bad = count_bad(ingredients, foods)
    return bad

assert part1(tfoods, tallergens) == 5
print(part1(foods, allergens))

# PART 2
def containment(ingredients):
    while any(len(value) != 1 for value in ingredients.values()):
        for alrg, ingr in ingredients.items():
            if len(ingr) == 1:
                for alrg2, ingr2 in ingredients.items():
                    if alrg == alrg2: continue
                    ingr2.difference_update(ingr)
    return ingredients

def part2(foods, allergens):
    ingredients = find_allergens(foods, allergens)
    ingredients = containment(ingredients)
    ingredients = {k: v for k, v in sorted(ingredients.items())}
    cdil = []
    for ingr in ingredients.values():
        cdil.append("".join(ingr))
    return ",".join(cdil)

assert part2(tfoods, tallergens) == "mxmxvkd,sqjhc,fvjkl"
print(part2(foods, allergens))

