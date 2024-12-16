import os
import re

sample_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

sample_input_2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

def get_puzzle_input() -> str:
    script_name = os.path.basename(__file__)
    day_number = script_name.split('-')[1].split('.')[0]
    return open(f"inputs/day-{day_number}.txt", "r").read()

def sum_all_mul_instructions(raw_input: str) -> int:
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = re.findall(pattern, raw_input)

    mul_sum = 0
    for mul in matches:
        mul_sum += int(mul[0]) * int(mul[1])
    return mul_sum

def sum_do_mul_instructions(raw_input: str) -> int:
    pattern = re.compile(r"don\'t\(\).*?(?=do\(\))", re.DOTALL)
    return sum_all_mul_instructions(pattern.sub("", raw_input))

print("\n# Part I: part_one_function\n")
print(f"sample input: {sum_all_mul_instructions(sample_input)}")
print(f"puzzle input: {sum_all_mul_instructions(get_puzzle_input())}")

print("\n# Part II: part_two_function\n")
wrong_answers_2 = {"too high":[103645239], "too low": [73659617]}
print(f"sample input: {sum_do_mul_instructions(sample_input_2)}")
print(f"puzzle input: {sum_do_mul_instructions(get_puzzle_input())}")

print(f"wrong answers only: {wrong_answers_2}")