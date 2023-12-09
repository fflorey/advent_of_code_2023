
file_path = "input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

nav_instructions = lines[0].strip()

data = {}
for line in lines[2:]:
    key, values = line.strip().split(" = ")
    values = tuple(values.strip("()").split(", "))
    data[key] = values

# all data[key] with a character 'A' in last position
def find_all_keys_with_A_in_last_position(data):
    result = []
    for key in data:
        if key[2] == 'A':
            result.append(key)
    return result

def find_all_keys_with_Z_in_last_position(data):
    result = []
    for key in data:
        if key[2] == 'Z':
            result.append(key)
    return result

def isEveyLastCharacterInListelementZ(list):
    for element in list:
        if element[-1] != 'Z':
            return False
    return True

print(find_all_keys_with_A_in_last_position(data))

print(find_all_keys_with_Z_in_last_position(data))

startlist = find_all_keys_with_A_in_last_position(data)

steps=0 
values=startlist
while True:
    if isEveyLastCharacterInListelementZ(values):
        break
    newValues=[]
    idx=steps%len(nav_instructions)
    nav=nav_instructions[idx]
    for value in values:
        plotL,plotR=data[value]
        # print("value: ", value)
        if nav=="R":
            newValues.append(plotR)
        elif nav=="L":
            newValues.append(plotL)
      
        # print ("nav: ", nav, "newvalues", newValues, "plotL: ", plotL, "plotR: ", plotR)
        
    steps+=1        
    if steps%100000==0:
        print(steps)

    values=newValues

print(steps)


