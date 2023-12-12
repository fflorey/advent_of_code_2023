lines = []
numbers = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(" ")
            lines.append(parts[0])
            numbers.append([int(num) for num in parts[1].split(",")])

print("List of lines:", lines)
print("List of numbers:", numbers)



def count_arrangements(spring_line, group_sizes):
    def is_valid(arrangement, group_sizes):
        size_idx = 0
        count = 0
        for spring in arrangement:
            if spring == '#':
                count += 1
            else:
                if count > 0:
                    if size_idx >= len(group_sizes) or count != group_sizes[size_idx]:
                        return False
                    size_idx += 1
                    count = 0
        return size_idx == len(group_sizes) and count == 0

    def backtrack(idx, current):
        if idx == len(spring_line):
            return 1 if is_valid(current, group_sizes) else 0

        if spring_line[idx] != '?':
            return backtrack(idx + 1, current + spring_line[idx])

        # Try both operational and broken spring
        return backtrack(idx + 1, current + '.') + backtrack(idx + 1, current + '#')

    return backtrack(0, "")

# Example usage
# line = ".?#???#???#.?.?##??"
# group_sizes = [6, 2, 1, 4]
for key, line in enumerate(lines):
    group_sizes = numbers[key]
    print(f"Number of arrangements for '{line}' and {group_sizes}: {count_arrangements(line, group_sizes)}")
