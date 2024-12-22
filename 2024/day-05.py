import json
import os
import re

sample_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def get_puzzle_input() -> str:
    script_name = os.path.basename(__file__)
    day_number = script_name.split('-')[1].split('.')[0]
    return open(f"inputs/day-{day_number}.txt", "r").read()

def parse_print_rules(raw_input: str) -> dict:
    pattern = re.compile(r"\b(\d+)\|(\d+)\b", re.DOTALL)
    raw_rules = pattern.findall(raw_input)
    print_rules: dict = {}
    for rule in raw_rules:
        if int(rule[0]) not in print_rules:
            print_rules[int(rule[0])]: list = []
        print_rules[int(rule[0])].append(int(rule[1]))
    return print_rules

def parse_updates(raw_input: str) -> list:
    pattern = re.compile(r"[\d\,]{3,}")
    raw_orders = pattern.findall(raw_input)
    print_orders: list = []

    for print_order in raw_orders:
        print_orders.append([int(num) for num in print_order.split(",")])

    return print_orders

def part_one_function(raw_input: str) -> int:
    rules = parse_print_rules(raw_input)
    updates = parse_updates(raw_input)

    valid_updates: list = []
    middle_page_sum = 0

    for update in updates:
        if not is_valid_update(update, rules):
            # print(f"invalid update: {update}")
            continue
        valid_updates.append(update)

    for update in valid_updates:
        # print(f"  valid update: {update} -> {get_middle_page(update)}")
        middle_page_sum += get_middle_page(update)

    return middle_page_sum

def is_valid_update(update: list, rules: dict) -> bool:
    for first_page in update:
        if not rules.get(first_page, False):
            continue

        for second_page in rules[first_page]:
            if second_page not in update:
                continue

            if update.index(first_page) > update.index(second_page):
                return False

    return True

def fails_rules(update: list, rules: dict) -> list:
    failed_rules: list[str] = []

    for first_page in update:
        if not rules.get(first_page, False):
            continue

        for second_page in rules[first_page]:
            if second_page not in update:
                continue

        if update.index(first_page) > update.index(second_page):
            failed_rules.append(f"page {first_page} comes after {second_page}")

    return failed_rules


def get_middle_page(update: list[int]) -> int:
    return update[int(len(update)/2)]

def part_two_function(raw_input: str) -> int:
    rules = parse_print_rules(raw_input)
    updates = parse_updates(raw_input)

    fixed_updates: list[list[int]] = []
    middle_page_sum = 0

    for update in updates:
        if is_valid_update(update, rules):
            continue

        while not is_valid_update(update, rules):
            update = fix_invalid_update(update=update, rules=rules)

        fixed_updates.append(update)

    for update in fixed_updates:
        middle_page_sum += get_middle_page(update)

    return middle_page_sum

def fix_invalid_update(update: list[int], rules: dict) -> list[int]:
    applicable_rules = get_applicable_rules(update, rules)

    for rule in applicable_rules:
        first_page, second_page = rule[0], rule[1]
        first_index = update.index(first_page)
        second_index = update.index(second_page)

        if first_index < second_index:
            continue

        update[second_index], update[first_index] = update[first_index], update[second_index]

    return update

def get_applicable_rules(update: list[int], rules: dict) -> list[list[int]]:
    applicable_rules: list[list[int]] = []
    for first_page, second_pages in rules.items():
        if first_page not in update:
            continue
        for second_page in second_pages:
            if second_page not in update:
                continue

            applicable_rules.append([first_page, second_page])

    return applicable_rules


print("\n# Part I: part_one_function\n")
print(f"sample input [143]: {part_one_function(sample_input)}")
print(f"puzzle input: {part_one_function(get_puzzle_input())}")

print("\n# Part II: part_two_function\n")
print(f"sample input [123]: {part_two_function(sample_input)}")
print(f"puzzle input: {part_two_function(get_puzzle_input())}")