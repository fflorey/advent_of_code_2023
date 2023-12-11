
def printLines(lines):
    for line in lines:
        print(line)

# lines is a list of tuples 
def insertAdditionalBlankLines(lines):
    tmp_lines = lines.copy()
    counter = 0
    for index, line in enumerate(lines):
        # if all elements in the line are "." then insert a blank line with n tuples of '.', length as the line
        if all(element == "." for element in line):
            tmp_lines.insert(index + counter, tuple("." for e in line))
            counter += 1
    return tmp_lines

def calcManhattanDistance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

file_path = "input.txt"
lines = []

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

rotated_lines = list(zip(*lines[::-1]))
rotated_lines = insertAdditionalBlankLines(rotated_lines)
rotated_lines = list(zip(*rotated_lines[::-1]))
rotated_lines = insertAdditionalBlankLines(rotated_lines)

printLines(rotated_lines)

galaxies=[]
for y, line in enumerate(rotated_lines):
    # find all the indices of '#' in the line and store y and the index in a tuple
    for x in [index for index, element in enumerate(line) if element == "#"]:
        galaxies.append((x, y))

print("Galaxies:", galaxies)

counter=0   
total_distance = 0
for index,g in enumerate(galaxies):
    for g2 in range(galaxies.index(g) + 1, len(galaxies)):
        counter += 1
        total_distance += calcManhattanDistance(g, galaxies[g2])
        

print("Counter:", counter, "Total distance:", total_distance)



