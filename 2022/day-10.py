import re
import math
import random

# Load sample data
sample_1 = """
noop
addx 3
addx -5
"""
sample_2 = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
sinput_1 = sample_1.strip()
sinput_2 = sample_2.strip()

# Load input file
input = open("inputs/day-10.txt", 'r').read().strip()

def parse_instruction(instruction):
    if re.fullmatch(r"^addx\s(\-?\d+)$", instruction):
        return int(re.findall(r"^addx\s(\-?\d+)$", instruction)[0])
    return "noop"

def run_instructions(instructions):
    cycle = 0
    instruction_count = len(instructions)
    instructions_ran = 0
    cycle_register_history = {}
    x_register = 1
    # print(f"running {instruction_count} instructions:")
    while instructions_ran < instruction_count:
        cycle += 1
        cycle_register_history[cycle] = {"start":x_register}
        # Start next execution
        result = parse_instruction(instructions[instructions_ran])
        if "noop" == result:
            cycle_register_history[cycle]["end"] = x_register
            cycle_register_history[cycle]["op"] = result
        else:
            cycle_register_history[cycle]["end"] = x_register
            cycle_register_history[cycle]["op"] = result
            cycle += 1
            cycle_register_history[cycle] = {"start":x_register}
            cycle_register_history[cycle]["op"] = result
            x_register += result
            cycle_register_history[cycle]["end"] = x_register
        instructions_ran += 1
        # print(f"cycle {cycle} instruction: {result:>4} ({x_register:>4})")
    return cycle_register_history

def run_instructions_old(instructions):
    cycle = 1
    instruction_count = len(instructions)
    instructions_ran = 0
    x_register = 1
    cycle_register_history = [x_register]
    current_instruction = None
    print(f"running {instruction_count} instructions:")
    while instructions_ran < instruction_count:
        cycle_register_history.append(x_register)
        result = parse_instruction(instructions[instructions_ran])
        if None == current_instruction:
            current_instruction = result
        else:
            if isinstance(result, int):
                x_register += result
            instructions_ran += 1
            current_instruction = None
        print(f"cycle {cycle} instruction: {result}")
        cycle += 1
    return cycle_register_history

def calculate_start_signal_strength(register_values, index):
    print(f"signal strength is {index} * {register_values[index]} = {index * register_values[index]['start']:>,}")
    return register_values[index]["start"] * index

def cursor_range(register_value=1):
    return list(range(register_value-1,register_value+2))

def print_row(register_values):
    row = ""
    type_line = " ........................................ "
    x_register = 1
    cursor_location = cursor_range()
    for c in range(1,len(register_values)):
        pixel = (c-1) % 40
        if pixel in cursor_location:
            # row += "#"
            row += "▓▓"
        else:
            # row += "."
            row += "░░"
        cursor_location = cursor_range(register_values[c]["end"])
        if 80 <= len(row):
            print(row)
            row = ""
    print(f"{row:░<80}")

print("########## start pt 1 ##########")
instructions = sinput_1.split("\n")
instructions = sinput_2.split("\n")
instructions = input.split("\n")
register_values = run_instructions(instructions)
print(register_values)
indecies = [20, 60, 100, 140, 180, 220]
total_signal_strength = 0
for index in indecies:
    total_signal_strength += calculate_start_signal_strength(register_values, index)
print(total_signal_strength)
print("---------- wrong answers ----------")
print({"too high":[26552,19280]})
print("========== end pt 1 ==========\n\n")

print("########## start pt 2 ##########")
print_row(register_values)
print("---------- wrong answers ----------")
print({"FGJRGCFK"})
print("========== end pt 2 ==========\n\n")
