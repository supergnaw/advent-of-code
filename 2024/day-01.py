import os
import re

sample_input = """3   4
4   3
2   5
1   3
3   9
3   3
"""

def get_puzzle_input() -> str:
    script_name = os.path.basename(__file__)
    day_number = script_name.split('-')[1].split('.')[0]
    return open(f"inputs/day-{day_number}.txt", "r").read()

def calculate_list_distance(raw_list: str) -> int:
    list_a: list = []
    list_b: list = []

    for row in raw_list.split("\n"):
        if not 0 < len(row.strip()):
            continue
        item_a, item_b = re.split("\s+", row, re.IGNORECASE)
        list_a.append(int(item_a))
        list_b.append(int(item_b))

    list_a.sort(key=None, reverse=False)
    list_b.sort(key=None, reverse=False)

    total_distance: int = 0

    for i in range(len(list_a)):
        diff: int = max(list_a[i], list_b[i]) - min(list_a[i], list_b[i])
        total_distance += diff

    return total_distance

def calculate_similarity_score(raw_list: str) -> int:
    list_a: list = []
    list_b: dict = {}

    for row in raw_list.split("\n"):
        if not 0 < len(row.strip()):
            continue
        item_a, item_b = re.split("\s+", row, re.IGNORECASE)
        item_b = int(item_b)
        list_a.append(int(item_a))

        if not list_b.get(item_b, False):
            list_b[item_b] = 0

        list_b[item_b] += 1

    total_similarity_score: int = 0

    for item_a in list_a:
        similarity_score: int = item_a * list_b.get(item_a, 0)
        total_similarity_score += similarity_score

    return total_similarity_score

print("\n# Calculate List Distance\n")
print(f"sample input: {calculate_list_distance(sample_input)}")
print(f"puzzle input: {calculate_list_distance(get_puzzle_input())}")

print("\n# Calculate Similarity Score\n")
print(f"sample input: {calculate_similarity_score(sample_input)}")
print(f"puzzle input: {calculate_similarity_score(get_puzzle_input())}")