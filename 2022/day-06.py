import re

sample = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""
input = sample.strip()

# Load input file
input = open("inputs/day-06.txt", 'r').read().strip()

def find_marker(input_string, marker_length):
    for position in range(0, len(input_string)):
        if marker_length == len(set(input_string[position:position+marker_length])):
            return position+marker_length, input_string[position:position+marker_length]


print("########## start pt 1 ##########")
for line in input.split("\n"):
    position, marker = find_marker(line, 4)
    print(f"marker in string {line}\n > {marker} ({position})")
print("---------- wrong answers ----------")
print({})
print("========== end pt 1 ==========\n\n")

print("########## start pt 2 ##########")
for line in input.split("\n"):
    position, marker = find_marker(line, 14)
    print(f"marker in string {line}\n > {marker} ({position})")
print("---------- wrong answers ----------")
print({})
print("========== end pt 2 ==========\n\n")
