
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

resultList=[]
steps=0 
total=1
values=startlist
print("values: ", values)
for value in values:
    # print("value: ", value)
    while value[2]!='Z':
        idx=steps%len(nav_instructions)
        nav=nav_instructions[idx]
        plotL,plotR=data[value]
        if nav=="R":
            value=plotR
        elif nav=="L":
            value=plotL
        steps+=1
        # print ("nav: ", nav, "value: ", value, "plotL: ", plotL, "plotR: ", plotR)
    print(steps)
    resultList.append(steps)
    steps=0

def find_greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def find_greatest_common_divisor_list(numbers):
    gcd = numbers[0]
    for i in range(1, len(numbers)):
        gcd = find_greatest_common_divisor(gcd, numbers[i])
    return gcd


print(resultList)
print(find_greatest_common_divisor_list(resultList))

last=resultList.pop(0)
while len(resultList)>0:
    current = resultList.pop(0)
    total=last*current
    total = total/find_greatest_common_divisor(last, current)
    print("Total: ", total, "last: ", last, "current: ", current)
    last=total


print(total)
