import re

sample = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
input = sample.strip()

# Load input file
input = open("inputs/day-07.txt", 'r').read().strip()

# Check if a line is changing to a directory: $ cd <directory-name>
def is_dir(line):
    return re.fullmatch(r"^\$\scd\s([^\s]+)$", line)

# Returns <directory-name>
def get_dir_data(line):
    return re.findall(r"^\$\scd\s([^\s]+)$", line)[0]

# Check if a line is listing a file size and file name: <intiger-value> <file-name>
def is_file(line):
    return re.fullmatch(r"^(\d+)\s([^\s]+)$", line)

# Returns <intiger-value>, <file-name>
def get_file_data(line):
    return re.findall(r"^(\d+)\s([^\s]+)$", line)[0]

# Returns /path/to/parent from /path/to/parent/child
def parse_parent(path):
    return path[0:path.rfind("/")].strip() if 0 < len(path[0:path.rfind("/")].strip()) else "/"

# Returns a list of all parent directory paths given a path
def parse_path_ancestry(parent_path):
    ancestors = []
    for i in range(0, parent_path.count("/")-1):
        parent_path = parse_parent(parent_path)
        ancestors.append(parse_parent(parent_path))
    return ancestors

# Parses console IO into dict of {"/path/to/dir":<dir-size>,...}
def parse_console_input(lines):
    directory_tree = {}
    current_path = ""

    # Loop through console lines
    for line in lines:
        if is_dir(line):
            # Get directory name
            dir_name = get_dir_data(line)
            # Go down one level
            if ".." != dir_name:
                # current_path = f"{current_path}/{dir_name}"
                current_path = f"{current_path}/{dir_name}".replace("//","/")
                if current_path not in directory_tree:
                    directory_tree[current_path] = 0
            # Go up one level
            else:
                # Change current path to parent directory
                current_path = parse_parent(current_path)
        # Add file size to directory
        elif is_file(line):
            file_size, file_name = get_file_data(line)
            directory_tree[current_path] += int(file_size)
    return directory_tree

# Fills in any missing ancestor directories and sorts entire tree by descending /dir/path/length
def sort_and_fill_out_directory_tree(directory_tree):
    dir_paths = directory_tree.keys()
    for dir_path in dir_paths:
        ancestors = parse_path_ancestry(dir_path)
        for dir_path in ancestors:
            if dir_path not in directory_tree:
                directory_tree[dir_path] = 0
                print(f"adding {dir_path} to directory_tree")

    sorted_directory_tree = {}
    for key in sorted(directory_tree, key=len, reverse=True):
        sorted_directory_tree[key] = directory_tree[key]

    return sorted_directory_tree

# Calculate actual size of directories based on child directories
def calculate_realsizes(directory_tree):
    for dir_path in directory_tree.keys():
        directory_tree[parse_parent(dir_path)] += directory_tree[dir_path]
    return directory_tree

# Sum directory sizes less than or equal to a given size limit
def sum_dirs_less_than(directory_tree, max_dir_size_for_summing):
    total_sum = 0
    remove_children = ""
    for dir_path in directory_tree:
        if max_dir_size_for_summing >= directory_tree[dir_path]:
            total_sum += directory_tree[dir_path]
            remove_children = dir_path
            break

    children_to_remove = []
    for dir_path in directory_tree:
        if remove_children == dir_path[0:len(remove_children)]:
            children_to_remove.append(dir_path)

    for dir_path in children_to_remove:
        directory_tree.pop(dir_path)

    if 0 < len(directory_tree):
        return total_sum + sum_dirs_less_than(directory_tree, max_dir_size_for_summing)
    return total_sum

# Sort directory tree by size of directory path
def sort_directory_tree_by_dir_size(directory_tree):
    return {k: v for k, v in sorted(directory_tree.items(), key=lambda item: item[1])}

# Find smallest directory greater than or equal to a given size limit
def find_smallest_directory_greater_than_or_equal_to(directory_tree, min_dir_size):
    for dir_path in directory_tree:
        if directory_tree[dir_path] >= min_dir_size:
            return dir_path, directory_tree[dir_path]


# Prep the vars
size_of_summed_dirs = 0
max_dir_size_for_summing = 100000
directory_tree = parse_console_input(input.strip().split("\n"))
sorted_directory_tree = sort_and_fill_out_directory_tree(directory_tree)
actual_size_directory_tree = calculate_realsizes(sorted_directory_tree)
print(f"directory_tree raw sizes: {directory_tree}")
print(f"sorted_directory_tree sizes: {sorted_directory_tree}")
print(f"actual_size_directory_tree sizes: {actual_size_directory_tree}")

total_sum = sum_dirs_less_than(actual_size_directory_tree, max_dir_size_for_summing)
print(f"dirs_to_sum: {total_sum}")
print("---------- wrong answers ----------")
print({1513209, 1969677, 1116292})
print("========== end pt 1 ==========\n\n")

print("########## start pt 2 ##########")
actual_size_directory_tree = calculate_realsizes(sort_and_fill_out_directory_tree(parse_console_input(input.strip().split("\n"))))
total_disk_space = 70000000
system_update_size = 30000000
total_disk_used = int(actual_size_directory_tree["/"]/2)
total_disk_available = total_disk_space - total_disk_used
update_space_required = system_update_size - total_disk_available
print(f"total_disk_space:      {total_disk_space:>12,}")
print(f"system_update_size:    {system_update_size:>12,}")
print(f"total_disk_used:       {total_disk_used:>12,}")
print(f"total_disk_available:  {total_disk_available:>12,}")
print(f"update_space_required: {update_space_required:>12,}")

directory_tree_sorted_by_dir_size = sort_directory_tree_by_dir_size(actual_size_directory_tree)
dir_path, dir_size = find_smallest_directory_greater_than_or_equal_to(directory_tree_sorted_by_dir_size, update_space_required)
print(f"> directory to delete: {dir_path:<12}")
print(f"> directory size:      {dir_size:>12,}")
print("---------- wrong answers ----------")
print({})
print("========== end pt 2 ==========")
