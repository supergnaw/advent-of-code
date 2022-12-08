import re

sample = """
30373
25512
65332
33549
35390
"""
input = sample.strip()

# Load input file
input = open("inputs/day-08.txt", 'r').read().strip()

def get_rows_and_columns(tree_array):
    tree_dict = {"rows":[],"columns":[]}
    for row in range(0, len(tree_array)):
        for column in range(0, len(tree_array[row])):
            # instantiations for nonsense error handling
            if row not in tree_dict["rows"]:
                tree_dict["rows"].append([])
            if column not in tree_dict["columns"]:
                tree_dict["columns"].append([])
            # add tree heights
            tree_dict["rows"][row].append(tree_array[row][column])
            tree_dict["columns"][column].append(tree_array[row][column])
    # clear out the empty lists from instantiations
    tree_dict["rows"] = list(filter(None, tree_dict["rows"]))
    tree_dict["columns"] = list(filter(None, tree_dict["columns"]))
    return tree_dict

def is_visible(tree_index, tree_list):
    # Outside trees are always visible
    # print(f"index {tree_index} [{tree_list[tree_index]}] in {tree_list}")
    visible_x = True if 0 == tree_index or tree_index == len(tree_list)-1 else False
    if visible_x:
        if 0 == tree_index:
            # print(f"[{str(tree_list[tree_index])}] {tree_list[tree_index + 1:]} | {visible_x}")
            pass
        else:
            # print(f"{tree_list[:tree_index]} [{str(tree_list[tree_index])}] | {visible_x}")
            pass
        return visible_x
    else:
        visible_a = True
        visible_b = True
        for height in range(int(tree_list[tree_index])-1, 10):
            if str(height+1) in tree_list[:tree_index]:
                visible_a = False
            if str(height+1) in tree_list[tree_index+1:]:
                visible_b = False
        # print(f"{tree_list[:tree_index]} [{str(tree_list[tree_index])}] {tree_list[tree_index+1:]} | {visible_a or visible_b or visible_x}")
    return visible_a or visible_b

def count_visible_trees(tree_rows, tree_columns):
    visible_count = 0
    for r in range(0, len(tree_rows)):
        for c in range(0, len(tree_columns)):
            if is_visible(c, tree_rows[r]) or is_visible(r, tree_columns[c]):
                # print(f"visible: {c}-{r}")
                visible_count += 1
    return visible_count

def calculate_scenic_score(tree_index, tree_list):
    # exterior trees always have a scenic score of zero
    if 0 == tree_index or tree_index == len(tree_list)-1:
        return 0
    # print(f"tree_list: {tree_list[:tree_index]} [{tree_list[tree_index]}] {tree_list[tree_index + 1:]} | index {tree_index} [{tree_list[tree_index]}]")
    score_a = 0
    score_b = 0
    # walk a
    for a in range(0, tree_index):
        # the elves might be able to see this far
        score_a += 1
        # just kidding, reset the quasiconnectivity counter
        if int(tree_list[tree_index]) <= int(tree_list[a]):
            score_a = 1
    # print(f"{tree_list[:tree_index]} [{tree_list[tree_index]}] | score: {score_a}")
    # walk b
    for b in range(tree_index+1, len(tree_list)):
        # the elves can definitely see this far
        score_b += 1
        # but not any further
        if int(tree_list[tree_index]) <= int(tree_list[b]):
            break
    # print(f"[{tree_list[tree_index]}] {tree_list[tree_index+1:]} | score: {score_b}")
    # print(f"- total: {score_a} * {score_b} = {score_a * score_b}")
    return score_a * score_b

def get_max_scenic_score(tree_rows, tree_columns):
    max_scenic_score = 0
    for r in range(0, len(tree_rows)):
        for c in range(0, len(tree_columns)):
            score_a = calculate_scenic_score(c, tree_rows[r])
            score_b = calculate_scenic_score(r, tree_columns[c])
            max_scenic_score = max(max_scenic_score, score_a * score_b)
    return max_scenic_score

def get_specific_scenic_score(r, c, tree_rows, tree_columns):
    score_a = calculate_scenic_score(c, tree_rows[r])
    score_b = calculate_scenic_score(r, tree_columns[c])
    return score_a * score_b

print("########## start pt 1 ##########")
tree_dict = get_rows_and_columns(input.split("\n"))
print(tree_dict)
num_visible = count_visible_trees(tree_dict["rows"], tree_dict["columns"])
print(f"num_visible: {num_visible}")
print("---------- wrong answers ----------")
print({2088})
print("========== end pt 1 ==========\n\n")

print("########## start pt 2 ##########")
# r = 3
# c = 2
# specific_scenic_score = get_specific_scenic_score(r, c, tree_dict["rows"], tree_dict["columns"])
# print(f"specific_scenic_score ({c}, {r}): {specific_scenic_score}")
max_scenic_score = get_max_scenic_score(tree_dict["rows"], tree_dict["columns"])
print(f"max_scenic_score: {max_scenic_score}")
print("---------- wrong answers ----------")
print({827008,671944})
print("========== end pt 2 ==========\n\n")
