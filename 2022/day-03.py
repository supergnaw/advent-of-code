import re

sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

# Load input file
input_03 = open("inputs/day-03.txt", 'r').read()
# input_03 = sample

def get_item_type_priority(item):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".rfind(item) + 1

def get_compartment_items(pack):
    return pack[:int(len(pack)/2)], pack[int(len(pack)/2):]

def find_unique_item_in_pack(compartment_1, compartment_2):
    for item in compartment_1:
        if item in compartment_2:
            return item

def find_common_item_in_packs(packs):
    packs = sorted(packs, key=len)
    for item in "".join(set(packs[0])):
        if item in packs[1] and item in packs[2]:
            return item

total_priorities_1 = 0
for pack in input_03.split("\n"):
    if 0 == len(pack.strip()):
        continue
    compartment_1, compartment_2 = get_compartment_items(pack)
    unique_item = find_unique_item_in_pack(compartment_1, compartment_2)
    priority = get_item_type_priority(unique_item)
    total_priorities_1 += priority
    print(f"{pack:<48} | {compartment_1:>24} x {compartment_2:<24} | {unique_item} ({priority})")
print("========== end pt 1 ==========")

total_priorities_2 = 0
packs = input_03.strip().split("\n")
for i in range(0, len(packs)):
    if 0 != i % 3: continue
    common_item = find_common_item_in_packs([packs[i], packs[i+1], packs[i+2]])
    priority = get_item_type_priority(common_item)
    total_priorities_2 += priority
    print(f"{packs[i]}\n{packs[i+1]}\n{packs[i+2]}\n > {unique_item} ({priority})")

print("========== end pt 2 ==========")
print(f"total_priorities_1: {total_priorities_1}")
print(f"total_priorities_2: {total_priorities_2}")
