import json
import os

sample_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def get_puzzle_input() -> str:
    script_name = os.path.basename(__file__)
    day_number = script_name.split('-')[1].split('.')[0]
    return open(f"inputs/day-{day_number}.txt", "r").read()

def xmas_word_search(raw_input: str, word: str = "XMAS") -> int:
    word_grid = [list(row) for row in raw_input.strip().split("\n")]
    word_count = 0
    boundary_top = len(word) - 2
    boundary_left = len(word) - 2
    boundary_right = len(word_grid[0]) - len(word) + 1
    boundary_bottom = len(word_grid) - len(word) + 1
    word_coordinates = []

    # loop through each row
    for r in range(len(word_grid)):
        # loop through each column
        for c in range(len(word_grid[r])):
            # instantiate new words for each new position
            up = ""
            up_right = ""
            right = ""
            right_down = ""
            down = ""
            down_left = ""
            left = ""
            left_up = ""

            for i in range(len(word)):
                if r > boundary_top:
                    up += word_grid[r - i][c]

                if r > boundary_top and c < boundary_right:
                    up_right += word_grid[r - i][c + i]

                if c < boundary_right:
                    right += word_grid[r][c + i]

                if r < boundary_bottom and c < boundary_right:
                    right_down += word_grid[r + i][c + i]

                if r < boundary_bottom:
                    down += word_grid[r + i][c]

                if r < boundary_bottom and c > boundary_left:
                    down_left += word_grid[r + i][c - i]

                if c > boundary_left:
                    left += word_grid[r][c - i]

                if r > boundary_top and c > boundary_left:
                    left_up += word_grid[r - i][c - i]

            if word == up:
                word_count += 1
                word_coordinates.append(f"row: {r}, col: {c}, direction: up '{up}")

            if word == up_right:
                word_count += 1
                word_coordinates.append(f"row: {r}, col: {c}, direction: up_right '{up_right}")

            if word == right:
                word_count += 1
                word_coordinates.append(f"row: {r}, col: {c}, direction: right '{right}")

            if word == right_down:
                word_count += 1
                word_coordinates.append(f"row: {r}, col: {c}, direction: right_down '{right_down}")

            if word == down:
                word_count += 1
                word_coordinates.append(f"row: {r}, col: {c}, direction: down '{down}")

            if word == down_left:
                word_count += 1
                word_coordinates.append(f"row: {r}, col: {c}, direction: down_left '{down_left}")

            if word == left:
                word_count += 1
                word_coordinates.append(f"row: {r}, col: {c}, direction: left '{left}")

            if word == left_up:
                word_count += 1
                word_coordinates.append(f"row: {r}, col: {c}, direction: left_up '{left_up}")

    # print(f"word coordinates [{len(word_coordinates)}]: {json.dumps(word_coordinates, indent=4)}")
    return word_count

def x_mas_search(raw_input: str, word: str = "MAS") -> int:
    word_grid = [list(row) for row in raw_input.strip().split("\n")]
    x_mas_count = 0
    boundary_top = len(word) - 2
    boundary_left = len(word) - 2
    boundary_right = len(word_grid[0]) - len(word) + 1
    boundary_bottom = len(word_grid) - len(word) + 1
    word_coordinates = []

    # loop through each row
    for r in range(len(word_grid)):
        if r < boundary_top or r > boundary_bottom:
            continue
        # loop through each column
        for c in range(len(word_grid[r])):
            if c < boundary_left or c > boundary_right:
                continue

            if "A" != word_grid[r][c]:
                continue

            words = [
                word_grid[r-1][c-1] + word_grid[r][c] + word_grid[r+1][c+1],
                word_grid[r-1][c+1] + word_grid[r][c] + word_grid[r+1][c-1],
                word_grid[r+1][c-1] + word_grid[r][c] + word_grid[r-1][c+1],
                word_grid[r+1][c+1] + word_grid[r][c] + word_grid[r-1][c-1],
            ]

            if 2 == len([mas for mas in words if "MAS" == mas]):
                x_mas_count += 1

    return x_mas_count

print("\n# Part I: part_one_function\n")
wrong_answers = {
    "too high": [2392, 2401]
}
print(f"sample input [18]: {xmas_word_search(sample_input)}")
print(f"puzzle input: {xmas_word_search(get_puzzle_input())}")

print(f"wrong answers only: {wrong_answers}")

print("\n# Part II: part_two_function\n")
print(f"sample input [9]: {x_mas_search(sample_input)}")
print(f"puzzle input: {x_mas_search(get_puzzle_input())}")