def read_calories(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n\n")
    return data

#calories = read_calories("test_input.txt") 
calories = read_calories("input.txt") 

calories_per_elf = [sum(map(int, calorie.strip().split("\n"))) for calorie in calories]
#PART 1
print(max(calories_per_elf))

#PART 2
print(sum(sorted(calories_per_elf, reverse=True)[:3]))
