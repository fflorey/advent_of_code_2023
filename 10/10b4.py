lines={}
with open("input.txt") as f:
    counter=0
    for line in f:
        lines[counter] = line.strip()
        counter+=1

MAX_X=len(lines[0])
MAX_Y=counter

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

def detectFieldsToOutside ( orig, image ):
    # orig and image are to dictionaries with the same size
    # orig and image are dictionaries which contains strings
    for y in range(len(orig)):
        counter_c1=0
        counter_c2=0
        out=True
        for x, char in enumerate(orig[y]):
            if image[y][x] == "P":
                if char == 'L':
                    counter_c1+=1
                if char == 'F':
                    counter_c2+=1
                if char == 'J':
                    counter_c1-=1
                if char == '7':
                    counter_c2-=1
                if char == '|':
                    out=not out
            if image[y][x] != "P":
                if counter_c1 != 0 or counter_c2 != 0:
                    out=not out
                    counter_c1=counter_c2=0
                if out:
                    image[y] = image[y][:x] + "O" + image[y][x+1:]
                    counter_c1=counter_c2=0
                else:
                    image[y] = image[y][:x] + "I" + image[y][x+1:]
                    counter_c1=counter_c2=0

    return image

def check_for_outside(MAX_X, MAX_Y, painting ):
    found = True
    while found:
        found = False
        for y in range(MAX_Y):
            for x in range(MAX_X):
                # if any of the four fields around the current field is "O", then the current field is outside
                if painting[y][x] != "P" and painting[y][x] != "O":
                    for field in [(x-1,y), (x,y-1), (x+1,y), (x,y+1),(x-1,y-1), (x+1,y-1), (x+1,y+1), (x-1,y+1)]:
                        if field[0] < 0 or field[1] < 0 or field[0] >= MAX_X or field[1] >= MAX_Y:
                            continue
                        if painting[field[1]][field[0]] == "O":
                            found = True
                            painting[y] = painting[y][:x] + "O" + painting[y][x+1:]
                            break

def mark_all_edge_fields_as_outside(MAX_X, MAX_Y, painting):
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if ( x == 0 or y == 0 or x == MAX_X-1 or y == MAX_Y-1 ):
                if painting[y][x] != "P":
                    painting[y] = painting[y][:x] + "O" + painting[y][x+1:]

print(findFirstHeading(lines))
direction,x,y = findFirstHeading(lines)
print("Direction:", direction, "x:", x, "y:", y)
print("lines[y][x]:", lines[y][x])

# find the way through the maze. We know, that the are no crossings or dead ends or bifurcations
# we can just go straight through the maze
counter = 0
path=[]
image=lines.copy()
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

    counter+=1
    nextChar = lines[y][x]
    fieldChar = lines[y][x]
    image[y] = image[y][:x] + "P" + image[y][x+1:]

    path.append(fieldChar)
    print("counter:", counter, "direction:", direction, "x:", x, "y:", y, "fieldChar:", fieldChar)
    if ( fieldChar == "S" ):
        print("found start again")
        break

# print image
for line in image.values():
    print(line)

# switch all not "P" to "."
for y in range(len(image)):
    for x, char in enumerate(image[y]):
        if char != "P":
            image[y] = image[y][:x] + "." + image[y][x+1:]

print("image after switch")

for line in image.values():
    print(line)

print("DETECT...")

neu = detectFieldsToOutside(lines, image)
mark_all_edge_fields_as_outside(MAX_X, MAX_Y, neu)
check_for_outside(MAX_X, MAX_Y, neu)
for line in neu.values():
    print(line)

# count all "I" in the image
counter=0
for y in range(len(neu)):
    for x, char in enumerate(neu[y]):
        if char == "I":
            counter+=1

print("counter:", counter)