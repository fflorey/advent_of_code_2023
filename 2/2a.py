file_path = "input.txt"

lines = []
with open(file_path, "r") as file:
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        lines.append(line)  # Store each line in the array

# Now you have all the lines stored in the 'lines' array
print(lines)


resultSet=dict()
for line in lines:
    # split the line by double point (:)
    # first element is the Game Id, store the second element in a variable
    line = line.split(":")
    gameid=line[0].strip().split(" ")[1]
    # Delete first word in gameid
    id=int(gameid)
    resultSet[id]=[]
    print ("Gameid: ",id)
    # split the second element in line by comma (colon)
    cs=line[1].strip().split(";")
    for cubeset in cs:
        cubeset=cubeset.strip()
        # split the cubeset by comma (colon)
        cubeset=cubeset.split(",")
        print(cubeset)
        r=0
        g=0
        b=0

        for cube in cubeset:
            cube=cube.strip()
            print("cube: ",cube)
            c2=cube.split(" ")    
            print(c2[0], c2[1])
            for color in ['red','green','blue']:
                print("color: ",color)
                if ( color == c2[1]):
                    print("Found color: ",color)
                    if ( color == 'red'):
                        r=int(c2[0])
                    elif ( color == 'green'):
                        g=int(c2[0])
                    elif ( color == 'blue'):
                        b=int(c2[0])
        resultSet[id].append([id,r,g,b])
        print("ResultSet: ",resultSet[id])


# print resultSet


maxValues = [-1,12,13,14]
resultID=0
print("ResultSet: ",resultSet)
for games in resultSet.values():
    print("Games: ",games)
    possible=True
    for game in games:
        print(game)
        if ( game[1] > maxValues[1]) or ( game[2] > maxValues[2]) or ( game[3] > maxValues[3]):            
            possible=False
            print("Not possible: ",game[0])
    if ( possible ):
        resultID+=game[0]

print("ResultID: ",resultID)

