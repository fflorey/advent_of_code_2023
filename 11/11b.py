
def printLines(lines):
    for line in lines:
        print(line)

# lines is a list of tuples 
def expandUniverseY(lines, galaxies, expansion):
    tmp_galaxies = []
    counter = 0
    empty_lines=[]
    for index, line in enumerate(lines):
        if all(element == "." for element in line):
            empty_lines.append(index)
    # add all galaxies before the first empty line
    y = empty_lines[0]
    for g in galaxies:
        if g[1] < y:
            tmp_galaxies.append((g[0], g[1]))
    for key,y in enumerate(empty_lines):
        counter += 1
        if key+1 >= len(empty_lines):
            y2 = 9999999999999999
        else:
            y2 = empty_lines[key+1]
        for g in galaxies:
            if g[1] > y and g[1] < y2:
            # add galaxy to tmp_galaxies and the expansion * counter to the y coordinate
                tmp_galaxies.append((g[0], g[1] + (expansion*counter)))

    return tmp_galaxies

# lines is a list of tuples 
def expandUniverseX(lines, galaxies, expansion):
    tmp_galaxies = []
    counter = 0
    empty_columns=[]
    # find all columns in lines, where all elements in the column are "."    
    for field in range(len(lines[0])):
        find=True    
        for line in lines:
            if line[field] != ".":
                find=False
                break
        if find:
            empty_columns.append(field)
    print("Empty columns:", empty_columns)
    # add all galaxies before the first empty column
    x = empty_columns[0]
    for g in galaxies:
        if g[0] < x:
            tmp_galaxies.append((g[0], g[1]))

    for key,x in enumerate(empty_columns):
        counter += 1
        if key+1 >= len(empty_columns):
            x2 = 9999999999999999
        else:
            x2 = empty_columns[key+1]
        for g in galaxies:
            if g[0] > x and g[0] < x2:
                # add galaxy to tmp_galaxies and the expansion * counter to the x coordinate
                tmp_galaxies.append((g[0] + (expansion*counter), g[1]))
    return tmp_galaxies


def findGalaxies(lines):
    galaxies=[]
    for y, line in enumerate(lines):
        # find all the indices of '#' in the line and store y and the index in a tuple
        for x in [index for index, element in enumerate(line) if element == "#"]:
            galaxies.append((x, y))
    return galaxies    

def calcManhattanDistance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

file_path = "input.txt"
lines = []
with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        lines.append(line)


# transform the lines into a list of tuples
tmp_l = []
for line in lines:
    tmp_l.append(tuple(line))
lines=tmp_l
galaxies = findGalaxies(lines)
galaxies = expandUniverseX(lines, galaxies, (1000000-1))
galaxies = expandUniverseY(lines, galaxies, (1000000-1))

counter=0   
total_distance = 0
for index,g in enumerate(galaxies):
    for g2 in range(galaxies.index(g) + 1, len(galaxies)):
        counter += 1
        total_distance += calcManhattanDistance(g, galaxies[g2])
        
print("Counter:", counter, "Total distance:", total_distance)
