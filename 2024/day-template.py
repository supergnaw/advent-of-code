import os

sample_input = """
paste_sample_input_here
"""

def get_puzzle_input() -> str:
    script_name = os.path.basename(__file__)
    day_number = script_name.split('-')[1].split('.')[0]
    return open(f"inputs/day-{day_number}.txt", "r").read()

def part_one_function(raw_input: str) -> int:
    return_variable = f"not implemented ({len(raw_input)})"
    return return_variable

def part_two_function(raw_input: str) -> int:
    return_variable = f"not implemented ({len(raw_input)})"
    return return_variable

print("\n# Part I: part_one_function\n")
print(f"sample input: {part_one_function(sample_input)}")
print(f"puzzle input: {part_one_function(get_puzzle_input())}")

print("\n# Part II: part_two_function\n")
print(f"sample input: {part_two_function(sample_input)}")
print(f"puzzle input: {part_two_function(get_puzzle_input())}")