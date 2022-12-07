sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

# Load input file
input = sample.strip()
input = open("inputs/day-04.txt", 'r').read().strip()

def a_contains_b(a, b):
    x, y = a.split("-")
    start_a, stop_a = min(int(x), int(y)), max(int(x), int(y))
    x, y = b.split("-")
    start_b, stop_b = min(int(x), int(y)), max(int(x), int(y))
    # print(f" > start_a: {start_a}, stop_a: {stop_a}, start_b: {start_b}, stop_b: {stop_b}")
    return start_a <= start_b and stop_a >= stop_b

def b_contains_a(a, b):
    x, y = a.split("-")
    start_a, stop_a = min(int(x), int(y)), max(int(x), int(y))
    x, y = b.split("-")
    start_b, stop_b = min(int(x), int(y)), max(int(x), int(y))
    # print(f" > start_a: {start_a}, stop_a: {stop_a}, start_b: {start_b}, stop_b: {stop_b}")
    return start_a >= start_b and stop_a <= stop_b

def one_contains_the_other(a, b):
    return a_contains_b(a, b) or b_contains_a(a, b)

def any_overlaps_any(a, b):
    x, y = a.split("-")
    start_a, stop_a = min(int(x), int(y)), max(int(x), int(y))
    x, y = b.split("-")
    start_b, stop_b = min(int(x), int(y)), max(int(x), int(y))
    # print(f"a ({a}): {start_a} to {stop_a}")
    # print(f"b ({b}): {start_b} to {stop_b}")
    # aaaaa-----  -----aaaaa
    # -----bbbbb  bbbbb-----
    if stop_a < start_b or stop_b < start_a:
        # print("- no overlap")
        return False
    # --aaaaa---  ---aaaaa--
    # ---bbbbb--  --bbbbb---
    if start_b <= stop_a <= stop_b or start_b <= start_a <= stop_b:
        # print("- yes overlap")
        return True
    # ---aa---  -aaaaaa-
    # -bbbbbb-  ---bb---
    return one_contains_the_other(a, b)

print("########## start pt 1 ##########")
count_of_one_contains_the_other = 0
for cleaning_pair in input.split("\n"):
    elf_1, elf_2 = cleaning_pair.strip().split(",")
    if one_contains_the_other(elf_1.strip(), elf_2.strip()):
        does_it_contain = "yes"
        count_of_one_contains_the_other += 1
    else:
        does_it_contain = "no"
    # print(f"{elf_1:>7} | {elf_2:<7} | {does_it_contain}")
print(f"count_of_one_contains_the_other: {count_of_one_contains_the_other}")
print("---------- wrong answers ----------")
print({})
print("========== end pt 1 ==========\n\n")

print("########## start pt 2 ##########")
count_of_any_overlap = 0
for cleaning_pair in input.split("\n"):
    elf_1, elf_2 = cleaning_pair.strip().split(",")
    if any_overlaps_any(elf_1, elf_2):
        count_of_any_overlap += 1
print(f"count_of_any_overlap: {count_of_any_overlap}")
print("========== end pt 2 ==========")
