lines={}
with open('input.txt') as f:
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

print("lines:", lines)
print(find_character_position(lines))

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

            

print(findFirstHeading(lines))
direction,x,y = findFirstHeading(lines)
print("Direction:", direction, "x:", x, "y:", y)
print("lines[y][x]:", lines[y][x])

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

    counter+=1
    nextChar = lines[y][x]
    fieldChar = lines[y][x]
    path.append(fieldChar)
    print("counter:", counter, "direction:", direction, "x:", x, "y:", y, "fieldChar:", fieldChar)
    if ( fieldChar == "S" ):
        print("found start again")
        break


print("counter:", counter)
print("Path: ", path)
half = int(len(path)/2)
print("half:", half)
print(path[half])

