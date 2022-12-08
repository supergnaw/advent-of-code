import re

sample = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
input = sample.rstrip()

# Load input file
input = open("inputs/day-05.txt", 'r').read()

def parse_stacks(input_text):
    character_map = []
    stacks = {}
    for line in input_text:
        if re.fullmatch(r"^[\s\d]+$", line):
            for column in stacks:
                stacks[column] = [crate for crate in list(reversed(stacks[column])) if crate.strip()]
            return stacks
        else:
            if 0 == len(line.strip()): continue
            piles = [line[i:i+4] for i in range(0, len(line), 4)]
            for i in range(1, len(piles)+1):
                if i not in stacks: stacks[i] = []
                stacks[i].append(piles[i-1][1])
    print(f"Error parsing stacks: {stacks}")

def parse_procedure(input_text, stacks):
    for line in input_text:
        line = line.strip()
        if not re.fullmatch(r"^move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$", line):
            continue
        quantity, from_stack, to_stack = re.findall(r"^move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$", line)[0]
        for moved in range(0, int(quantity)):
            crate = stacks[int(from_stack)].pop()
            stacks[int(to_stack)].append(crate)
    return stacks

def get_top_crates(post_procedure_stacks):
    crates = []
    for stack in post_procedure_stacks:
        crates.append(post_procedure_stacks[stack].pop())
    return "".join(crates)

def parse_procedure_9001(input_text, stacks):
    for line in input_text:
        line = line.strip()
        if not re.fullmatch(r"^move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$", line):
            continue
        quantity, from_stack, to_stack = re.findall(r"^move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$", line)[0]
        moved_crates = stacks[int(from_stack)][-int(quantity):]
        stacks[int(from_stack)] = stacks[int(from_stack)][0:-int(quantity)]
        stacks[int(to_stack)] += moved_crates
    return stacks

print("########## start pt 1 ##########")
input_text = input.split("\n")
initial_stacks = parse_stacks(input_text)
print(f"initial_stacks: {initial_stacks}")
finished_stacks = parse_procedure(input_text, initial_stacks)
print(f"finished_stacks: {finished_stacks}")
top_crates = get_top_crates(finished_stacks)
print(f"top_crates: {top_crates}")
print("---------- wrong answers ----------")
print({})
print("========== end pt 1 ==========\n\n")

print("########## start pt 2 ##########")
initial_stacks = parse_stacks(input_text)
print(f"initial_stacks: {initial_stacks}")
finished_stacks = parse_procedure_9001(input_text, initial_stacks)
print(f"finished_stacks: {finished_stacks}")
top_crates = get_top_crates(finished_stacks)
print(f"top_crates: {top_crates}")
print("---------- wrong answers ----------")
print({})
print("========== end pt 2 ==========\n\n")
