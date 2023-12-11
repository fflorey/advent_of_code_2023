lines={}
with open('input.txt') as f:
    counter=0
    for line in f:
        lines[counter] = line.strip()
        counter+=1

MAX_X=len(lines[0])
MAX_Y=counter

painting = lines.copy()
painting_anti_clockwise = lines.copy()


def find_character_position(lines, character="S"):
    for y in range(len(lines)):
        for x, char in enumerate(lines[y]):
            if char == character:
                return x, y
    return None


def findFirstHeading(lines):
    x, y = find_character_position(lines)
    searchFields = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for direction, field in enumerate(searchFields):
        nx=x+field[0]
        ny=y+field[1]
        if ny >= 0 and ny < MAX_Y and nx < MAX_X and nx >= 0:
            fieldChar = lines[y + field[1]][x + field[0]]
            print("fieldChar:", fieldChar, "direction:", direction)
            if fieldChar == ".":
                continue
            if direction == 0:
                print("north")
                if fieldChar == "|" or fieldChar == "F" or fieldChar == "7":
                    print("found")
                    return direction,x,y
            elif direction == 1:
                print("east")
                if fieldChar == "-" or fieldChar == "J" or fieldChar == "7":
                    print("found")
                    return direction,x,y
            elif direction == 2:                
                print("south")
                if fieldChar == "|" or fieldChar == "L" or fieldChar == "J":
                    print("found")
                    return direction,x,y
            elif direction == 3:
                print("west")
                if fieldChar == "-" or fieldChar == "7" or fieldChar == "J":
                    print("found")
                    return direction,x,y

    return "impossible",-1,-1

        
def mark_as_outside_clockwise(MAX_X, MAX_Y, painting, direction, x, y, field):
    print ("y:", y, "x:", x, "d: ", direction)
    print("Current Field: ", field[y][x])
    if ( direction == 0 ):
        if ( x > 0 ):
            if ( field[y][x-1] != "P" ):
                painting[y] = painting[y][:x-1] + "O" + painting[y][x:]            
    elif ( direction == 1 ):
        if ( y > 0 ):
            if ( field[y-1][x] != "P" ):
                painting[y-1] = painting[y-1][:x] + "O" + painting[y-1][x+1:]            

    elif ( direction == 2 ):
        for d in range(0,2):
            if ( x+1 < MAX_X and y+d >= 0 and y+d < MAX_Y ):
                if ( painting[y+d][x+1] != "P" ):
                    painting[y+d] = painting[y+d][:x+1] + "O" + painting[y+d][x+2:]
    elif ( direction == 3 ):
        for d in range(0,2):
            if ( x+d < MAX_X and x+d > 0 and y+1 < MAX_Y  ):
                if ( painting[y+1][x+d] != "P" ):
                    painting[y+1] = painting[y+1][:x+d] + "O" + painting[y+1][x+d+1:]


def mark_as_outside_anticlockwise(MAX_X, MAX_Y, field, direction, x, y, currentField):
    if ( direction == 0 ):
        if ( x < MAX_X-1 ):
            if ( field[y][x+1] != "P" ):
                field[y] = field[y][:x+1] + "O" + field[y][x+2:]
    elif ( direction == 1 ):
        if ( y < MAX_Y-1 ):
            if ( field[y+1][x] != "P" ):
                field[y+1] = field[y+1][:x] + "O" + field[y+1][x+1:]

    elif ( direction == 2 ):
        if ( x > 0 ):
            if ( field[y][x-1] != "P" ):
                field[y] = field[y][:x-1] + "O" + field[y][x:]
    elif ( direction == 3 ):
        if ( y > 0 ):
            if ( field[y-1][x] != "P" ):
                field[y-1] = field[y-1][:x] + "O" + field[y-1][x+1:]


def check_for_outside(MAX_X, MAX_Y, painting ):
    for y in range(MAX_Y):
        for x in range(MAX_X):
            # if any of the four fields around the current field is "O", then the current field is outside
            if painting[y][x] != "P" and painting[y][x] != "O":
                if ( x > 0 ):
                    if ( painting[y][x-1] == "O" ):
                        painting[y] = painting[y][:x] + "O" + painting[y][x+1:]
                        continue
                if ( y > 0 ):
                    if ( painting[y-1][x] == "O" ):
                        painting[y] = painting[y][:x] + "O" + painting[y][x+1:]
                        continue
                if ( x < MAX_X-1 ):
                    if ( painting[y][x+1] == "O" ):
                        painting[y] = painting[y][:x] + "O" + painting[y][x+1:]
                        continue
                if ( y < MAX_Y-1 ):
                    if ( painting[y+1][x] == "O" ):
                        painting[y] = painting[y][:x] + "O" + painting[y][x+1:]
                        continue

def count_all_outside_fields(MAX_X, MAX_Y, painting):
    outsideFields = 0
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if painting[y][x] == "O":
                outsideFields += 1
    return outsideFields

# count all fields which are not "P" or "O"
def count_all_inside_fields(MAX_X, MAX_Y, painting):
    insideFields = 0
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if painting[y][x] != "O" and painting[y][x] != "P":
                insideFields += 1
    return insideFields

def mark_all_edge_fields_as_outside(MAX_X, MAX_Y, painting):
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if ( x == 0 or y == 0 or x == MAX_X-1 or y == MAX_Y-1 ):
                if painting[y][x] != "P":
                    painting[y] = painting[y][:x] + "O" + painting[y][x+1:]


direction,x,y = findFirstHeading(lines)
print("Direction:", direction, "x:", x, "y:", y)
print("lines[y][x]:", lines[y][x])
painting[y] = painting[y][:x] + "P" + painting[y][x+1:]
painting_anti_clockwise[y] = painting_anti_clockwise[y][:x] + "P" + painting_anti_clockwise[y][x+1:]
# find the way through the maze. We know, that the are no crossings or dead ends or bifurcations
# we can just go straight through the maze
counter = 0
path=[]
while True:
    print("X:", x, "Y:", y, "direction:", direction)
    if ( direction == 0 ):
        y -= 1
        nextChar = lines[y][x]
        print("d0: nextChar:", nextChar)
        if ( nextChar == "|" ):
            direction = 0
        if ( nextChar == "F" ):
            direction = 1
        if ( nextChar == "7" ):
            direction = 3        
    elif ( direction == 1 ):
        x += 1  
        nextChar = lines[y][x]
        print("d1 nextChar:", nextChar)
        if ( nextChar == "-"  ):
            direction = 1
        if ( nextChar == "J" ):
            direction = 0
        if ( nextChar == "7" ):
            direction = 2
    elif ( direction == 2 ):
        y += 1
        nextChar = lines[y][x]
        print("d2 nextChar:", nextChar)
        if ( nextChar == "|" ):
            direction = 2
        if ( nextChar == "L" ):
            print("found L")
            direction = 1
        if ( nextChar == "J" ):
            direction = 3
    elif ( direction == 3 ):
        x -= 1
        nextChar = lines[y][x]
        print("d3 nextChar:", nextChar)
        if ( nextChar == "-" ):
            direction = 3
        if ( nextChar == "L" ):
            direction = 0
        if ( nextChar == "F" ):
            direction = 2

    counter += 1
    nextChar = lines[y][x]
    # set the field to "O" to mark it as visited in painting
    painting[y] = painting[y][:x] + "P" + painting[y][x+1:]
    painting_anti_clockwise[y] = painting_anti_clockwise[y][:x] + "P" + painting_anti_clockwise[y][x+1:]
    # place a "O" on the painting field, on the left side of my path, as i 
    # walk through the maze clockwise - so on the left side, area cant be enclosed 
    # by the path. If there is a "P" on the left side, we do nothing
    # mark_as_outside_clockwise(MAX_X, MAX_Y, painting, direction, x, y)
    # mark_as_outside_anticlockwise(MAX_X, MAX_Y, painting_anti_clockwise, direction, x, y)

    
    fieldChar = lines[y][x]
    path.append(fieldChar)
    if ( fieldChar == "S" ):
        break


print("Counter: ", counter)

for l in painting.values():
    print(l)

input()

################ first round ended

direction,x,y = findFirstHeading(lines)
print("Direction:", direction, "x:", x, "y:", y)
print("lines[y][x]:", lines[y][x])
painting[y] = painting[y][:x] + "P" + painting[y][x+1:]
painting_anti_clockwise[y] = painting_anti_clockwise[y][:x] + "P" + painting_anti_clockwise[y][x+1:]
# find the way through the maze. We know, that the are no crossings or dead ends or bifurcations
# we can just go straight through the maze
counter = 0
path=[]
while True:
    if ( direction == 0 ):
        y -= 1
        nextChar = lines[y][x]
        print("d0: nextChar:", nextChar)
        if ( nextChar == "|" ):
            direction = 0
        if ( nextChar == "F" ):
            direction = 1
        if ( nextChar == "7" ):
            direction = 3        
    elif ( direction == 1 ):
        x += 1  
        nextChar = lines[y][x]
        print("d1 nextChar:", nextChar)
        if ( nextChar == "-"  ):
            direction = 1
        if ( nextChar == "J" ):
            direction = 0
        if ( nextChar == "7" ):
            direction = 2
    elif ( direction == 2 ):
        y += 1
        nextChar = lines[y][x]
        print("d2 nextChar:", nextChar)
        if ( nextChar == "|" ):
            direction = 2
        if ( nextChar == "L" ):
            print("found L")
            direction = 1
        if ( nextChar == "J" ):
            direction = 3
    elif ( direction == 3 ):
        x -= 1
        nextChar = lines[y][x]
        print("d3 nextChar:", nextChar)
        if ( nextChar == "-" ):
            direction = 3
        if ( nextChar == "L" ):
            direction = 0
        if ( nextChar == "F" ):
            direction = 2

    counter += 1
    currentField = nextChar
    nextChar = lines[y][x]
    # set the field to "O" to mark it as visited in painting
    painting[y] = painting[y][:x] + "P" + painting[y][x+1:]
    painting_anti_clockwise[y] = painting_anti_clockwise[y][:x] + "P" + painting_anti_clockwise[y][x+1:]
    # place a "O" on the painting field, on the left side of my path, as i 
    # walk through the maze clockwise - so on the left side, area cant be enclosed 
    # by the path. If there is a "P" on the left side, we do nothing
    mark_as_outside_clockwise(MAX_X, MAX_Y, painting, direction, x, y, lines)
    mark_as_outside_anticlockwise(MAX_X, MAX_Y, painting_anti_clockwise, direction, x, y, lines)

    print("Clockwise")  
    for l in painting.values():
        print(l)
    print("Anti Clockwise")
    for l in painting_anti_clockwise.values():
        print(l)
    input()
    
    fieldChar = lines[y][x]
    path.append(fieldChar)
    print("counter:", counter, "direction:", direction, "x:", x, "y:", y, "fieldChar:", fieldChar)
    if ( fieldChar == "S" ):
        print("found start again")
        break


################ sec round ended

# replace_all_noisy_fields(MAX_X, MAX_Y, painting)
# replace_all_noisy_fields(MAX_X, MAX_Y, painting_anti_clockwise)

print("Clockwise")  
for l in painting.values():
    print(l)
print("Anti Clockwise")
for l in painting_anti_clockwise.values():
    print(l)


mark_all_edge_fields_as_outside(MAX_X, MAX_Y, painting)
mark_all_edge_fields_as_outside(MAX_X, MAX_Y, painting_anti_clockwise)


orig_outsides=-1
outsides = 0
while outsides != orig_outsides:
    orig_outsides = outsides
    check_for_outside(MAX_X, MAX_Y, painting)
    outsides=count_all_outside_fields(MAX_X, MAX_Y, painting)
    print("outsides clockwise:", outsides, "orig_outsides:", orig_outsides)


orig_outsides=-1
outsides = 0
while outsides != orig_outsides:
    orig_outsides = outsides
    check_for_outside(MAX_X, MAX_Y, painting_anti_clockwise)
    outsides=count_all_outside_fields(MAX_X, MAX_Y, painting_anti_clockwise)
    print("outsides anticlockwise:", outsides, "orig_outsides:", orig_outsides)

print("Clockwise")
for l in painting.values():
    print(l)
print("Anti Clockwise")
for l in painting_anti_clockwise.values():
    print(l)


print("All Inside Fields clockwise:", count_all_inside_fields(MAX_X, MAX_Y, painting))
print("All Inside Fields: anticlockwise", count_all_inside_fields(MAX_X, MAX_Y, painting_anti_clockwise))
