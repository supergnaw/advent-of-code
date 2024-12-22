import json
import os

sample_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def get_puzzle_input() -> str:
    script_name = os.path.basename(__file__)
    day_number = script_name.split('-')[1].split('.')[0]
    return open(f"inputs/day-{day_number}.txt", "r").read()


def parse_puzzle_input(raw_input: str) -> list[list[str]]:
    map_list = []
    for row in raw_input.strip().split("\n"):
        map_list.append([column for column in list(row.strip())])
    return map_list


def part_one_function(raw_input: str) -> int:
    situation_map = parse_puzzle_input(raw_input)

    while not isinstance(situation_map, int):
        situation_map = move_guard(situation_map)

        if isinstance(situation_map, list):
            print("\n" + "=" * 80 + "\n".join(["".join(row) for row in situation_map]))

    return situation_map


def move_guard(situation_map) -> list or int:
    top_bound = 0
    right_bound = len(situation_map[0]) - 1
    bottom_bound = len(situation_map) - 1
    left_bound = 0

    directions = {
        "^": "up",
        ">": "right",
        "v": "down",
        "<": "left"
    }

    turn_direction = {
        "up": ">",
        "right": "v",
        "down": "<",
        "left": "^"
    }

    x_count = 0

    for r, row in enumerate(situation_map):
        for c, column in enumerate(situation_map[r]):
            # count the Xs just because
            if "X" == situation_map[r][c]:
                x_count += 1

            # check if guard, skip if not
            direction = directions.get(situation_map[r][c], False)
            if not direction:
                continue

            # get next spot
            next_r = r
            next_c = c
            if "up" == direction:
                next_r -= 1
            elif "right" == direction:
                next_c += 1
            elif "down" == direction:
                next_r += 1
            elif "left" == direction:
                next_c -= 1

            # check if next spot is exit
            if next_r < top_bound or next_r > bottom_bound or next_c < left_bound or next_c > right_bound:
                situation_map[r][c] = "X"
                return situation_map

            # check for obstruction and turn guard
            if "#" == situation_map[next_r][next_c]:
                situation_map[r][c] = turn_direction[direction]
                return situation_map

            # if no obstruction, advance
            situation_map[next_r][next_c] = str(situation_map[r][c])
            situation_map[r][c] = "X"
            return situation_map

    return x_count


def part_two_function(raw_input: str) -> int:
    return_variable = f"not implemented ({len(raw_input)})"
    return return_variable


print("\n# Part I: part_one_function\n")
print(f"sample input [41]: {part_one_function(sample_input)}")
print(f"puzzle input: {part_one_function(get_puzzle_input())}")

# print("\n# Part II: part_two_function\n")
# print(f"sample input: {part_two_function(sample_input)}")
# print(f"puzzle input: {part_two_function(get_puzzle_input())}")
