import re
import math
import random
# Load sample data
sample = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
sample_2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
input_s1 = sample.strip()
input_s2 = sample_2.strip()

# Load input file
input = open("inputs/day-09.txt", 'r').read().strip()

def parse_vector(line_input):
    return re.findall(r"^([UDLR])\s+(\d+)$", line_input)[0][0], int(re.findall(r"^([UDLR])\s+(\d+)$", line_input)[0][1])

def calc_distance(c1, c2):
    return math.sqrt(((c2[0]-c1[0])*(c2[0]-c1[0]))+((c2[1]-c1[1])*(c2[1]-c1[1])))

def move_rope(head, tail, vector, visits):
    x_h, y_h = head
    x_t, y_t = tail
    direction, distance = parse_vector(vector.strip())
    for step in range(distance):
        if "U" == direction: y_h += 1
        if "D" == direction: y_h -= 1
        if "L" == direction: x_h -= 1
        if "R" == direction: x_h += 1
        head = (x_h, y_h)
        if 1.5 < calc_distance(head, tail):
            if 2 < calc_distance(head, tail):
                # diagonal
                x_t = x_t + 1 if x_h > x_t else x_t - 1
                y_t = y_t + 1 if y_h > y_t else y_t - 1
            elif x_t == x_h:
                y_t = y_t + 1 if y_h > y_t else y_t - 1
            elif y_t == y_h:
                x_t = x_t + 1 if x_h > x_t else x_t - 1
            tail = (x_t, y_t)
            if tail not in visits:
                visits.append(tail)
    return head, tail, visits

def move_long_rope(segments, vector, visits):
    direction, distance = parse_vector(vector.strip())
    print(f"Move {direction} {distance} spaces")
    for step in range(1,distance+1):
        x_1, y_1 = segments[0]
        if "U" == direction:
            # print(f"Move y_1 {direction} [{y_1} + 1 = {y_1 + 1}]:")
            y_1 += 1
        elif "D" == direction:
            # print(f"Move y_1 {direction} [{y_1} - 1 = {y_1 - 1}]:")
            y_1 -= 1
        elif "L" == direction:
            # print(f"Move x_1 {direction} [{x_1} - 1 = {x_1 - 1}]:")
            x_1 -= 1
        elif "R" == direction:
            # print(f"Move x_1 {direction} [{x_1} + 1 = {x_1 + 1}]:")
            x_1 += 1
        segments[0] = (x_1, y_1)
        # print(f"{step} ({direction}): {segments[0]}")
        for s in range(1, len(segments)):
            x_1, y_1 = segments[s-1]
            x_2, y_2 = segments[s]
            # Max legal diagonal distance is 1.4 (2^.5)
            if 1.5 < calc_distance(segments[s-1], segments[s]):
                # if distance is 2.2 or more, it was diagonal, and moved diagonal again
                if 2 < calc_distance(segments[s-1], segments[s]):
                    x_2 = x_2 + 1 if x_1 > x_2 else x_2 - 1
                    y_2 = y_2 + 1 if y_1 > y_2 else y_2 - 1
                # if x is the same, it moved vertically
                elif x_2 == x_1:
                    y_2 = y_2 + 1 if y_1 > y_2 else y_2 - 1
                # if y is the same, it moved horizontally
                elif y_2 == y_1:
                    x_2 = x_2 + 1 if x_1 > x_2 else x_2 - 1
                segments[s] = (x_2, y_2)
            if s == len(segments) - 1 and segments[s] not in visits:
                visits.append(segments[s])
    print_rope(segments)
    return segments, visits

def print_rope(segments, x_min = 1000, y_min = 1000, x_max = -1000, y_max = -1000):
    char_map = ["H"] + list(range(1, len(segments)+1))
    rows = []
    for segment in segments:
        x_min = min(segment[0], x_min)
        x_max = max(segment[0], x_max)
        y_min = min(segment[1], y_min)
        y_max = max(segment[1], y_max)
    for y in range(y_min, y_max + 1):
        row = ""
        for x in range(x_min, x_max + 1):
            row += str(char_map[segments.index((x,y))])[-1] if (x,y) in segments else "."
        rows.append(row)
    print("==========")
    for row in list(reversed(rows)):
        print(f"{row}")
    print("==========")


print("########## start pt 1 ##########")
head = (0,0)
tail = (0,0)
visits = [(0,0)]
for direction in input.split("\n"):
    head, tail, visits = move_rope(head, tail, direction, visits)
print(len(visits))
print("---------- wrong answers ----------")
print({})
print("========== end pt 1 ==========\n\n")

print("########## start pt 2 ##########")
segments = [(0,0)]*10
visits = [(0,0)]
for direction in input_s2.split("\n"):
    segments, visits = move_long_rope(segments, direction, visits)
print(len(visits))
segments = [(0,0)]*11
visits = [(0,0)]
for direction in input.split("\n"):
    segments, visits = move_long_rope(segments, direction, visits)
print(len(visits))
print("---------- wrong answers ----------")
print({269, 217, 2483})
print("========== end pt 2 ==========\n\n")
