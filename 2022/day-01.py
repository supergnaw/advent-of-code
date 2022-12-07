# Load input_01 file
input_01 = open("inputs/day-01.txt", 'r').read()

# Parsing Function
def parse_input(input):
    elf_food_list = []
    max_calories_an_elf_is_carrying = 0
    elf_total_calorie_list = []
    for food_items in input_01.split("\n\n"):
        items_this_elf_is_carrying = food_items.split("\n")
        calories_this_elf_is_carrying = sum([int(i) for i in items_this_elf_is_carrying if type(i)== int or i.isdigit()])
        max_calories_an_elf_is_carrying = max(calories_this_elf_is_carrying, max_calories_an_elf_is_carrying)
        elf_food_list.append(items_this_elf_is_carrying)
        elf_total_calorie_list.append(calories_this_elf_is_carrying)
    elf_total_calorie_list = sorted(elf_total_calorie_list)
    top_three_calories_sum = sum(elf_total_calorie_list[-3:])
    return max_calories_an_elf_is_carrying, top_three_calories_sum

# Parse input
max_calories_an_elf_is_carrying, top_three_calories_sum = parse_input(input_01)
print(f"max_calories_an_elf_is_carrying: {max_calories_an_elf_is_carrying}")
print(f"top_three_calories_sum: {top_three_calories_sum}")
