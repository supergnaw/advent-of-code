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
        if rule[0] not in print_rules.keys():
            print_rules[rule[0]]: list = []
        print_rules[rule[0]].append(rule[1])
    return print_rules

def updates(raw_input: str) -> list:
    pattern = re.compile(r"[\d\,]{3,}")
    raw_orders = pattern.findall(raw_input)
    print_orders: list = []

    for print_order in raw_orders:
        print_orders.append([int(num) for num in print_order.split(",")])

    return print_orders

def part_one_function(raw_input: str) -> int:
    rules = parse_print_rules(raw_input)
    orders = updates(raw_input)
    print(f"rules for pages: {rules.keys()}")

    for order in orders:
        print(f"order: {order}")
        if not passes_order_rules(order, rules):
            print(f"invalid update: {order}")
            continue
        print(f"valid update: {order}")
    return 0

def passes_order_rules(update: list, rules: dict) -> bool:
    for page, before in rules.items():
        if page not in update:
            continue
        print(f"page {page} is in update: {update}")
        for p in before:
            if page not in update or p not in update:
                continue
            if update.index(before) < update.index(page):
                return False
    return True


def get_middle_page(order) -> int:
    return order[-int(len(order) / 2)]

def part_two_function(raw_input: str) -> int:
    puzzle_input = parse_puzzle_input(raw_input)
    return 0

print("\n# Part I: part_one_function\n")
print(f"sample input: {part_one_function(sample_input)}")
# print(f"puzzle input: {part_one_function(get_puzzle_input())}")

print("\n# Part II: part_two_function\n")
# print(f"sample input: {part_two_function(sample_input)}")
# print(f"puzzle input: {part_two_function(get_puzzle_input())}")