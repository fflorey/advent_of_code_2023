lines = []
numbers = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(" ")
            lines.append(parts[0])
            numbers.append([int(num) for num in parts[1].split(",")])

def replace_questionmarks(line, arrangement):
    new_line = ""
    idx = 0
    for char in line:
        if char == '?':
            if arrangement[idx] == '0':
                new_line += '.'
            else:
                new_line += '#'
            idx += 1
        else:
            new_line += char
    return new_line

def check_valid(line, group_sizes):
    # print ("Checking if valid:", line, "with group sizes:", group_sizes)
    groups_counter = len(group_sizes)
    group_count = 0
    current_group = 0
    group_idx = 0
    for i,char in enumerate(line):
        if char == '#':
            if current_group == 0:
                group_idx += 1
            current_group += 1            
        elif char == '.':
            if current_group > 0:
                group_count += 1
                if groups_counter < group_idx:
                    return False
                if current_group != group_sizes[group_idx-1]:
                    # print("Group size mismatch:", current_group, "!=", group_sizes[group_idx-1])
                    return False
                current_group = 0
        # print("i:", i, "char:", char, "current_group:", current_group, "group_count:", group_count, "group_idx:", group_idx)
    # Check if there is a group at the end of the line
    if current_group > 0:
        group_count += 1
        if groups_counter < group_idx:
            return False
        if current_group != group_sizes[group_idx-1]:
            # print("Group size mismatch:", current_group, "!=", group_sizes[group_idx-1])
            return False
    # print("Number of groups of '#':", group_count)
    # print("Number of groups expected:", groups_counter)
    return group_count == groups_counter


result = 0
total=0
for key, line in enumerate(lines):
    # print("now part A")
    print ("Line:", line, "with group sizes:", numbers[key])
    line = line + "."
    line = line * 3
    numbers[key] = numbers[key] * 3
    # print ("Check Line:", line, "with group sizes:", numbers[key])
    group_sizes = numbers[key]
    number_questionmarks = line.count('?')
    # print("Number of questionmarks:", number_questionmarks)
    max = 2 ** number_questionmarks
    # print("Check max:", max)
    correct_results = []
    for i in range(max):
        possible_arrangement = bin(i)[2:].zfill(number_questionmarks) 
        new_line = replace_questionmarks(line, possible_arrangement)

        # check if new_line is valid
        if check_valid(new_line, group_sizes):
            total += 1
            # print("VALID! ", new_line, "total:", total)
            # print("The correct arrangement is:", possible_arrangement)
            correct_results.append(i)
    print ("Found in total", total, "valid arrangements")
    total = 0



print("Total: ", result)