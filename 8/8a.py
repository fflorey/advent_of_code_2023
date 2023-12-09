
file_path = "input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

nav_instructions = lines[0].strip()

data = {}
for line in lines[2:]:
    key, values = line.strip().split(" = ")
    values = tuple(values.strip("()").split(", "))
    data[key] = values

# find ZZZ in data, when starting at first value
steps=0 
value="AAA"
while value!="ZZZ":
    idx=steps%len(nav_instructions)
    nav=nav_instructions[idx]
    plotL,plotR=data[value]
    if nav=="R":
        value=plotR
    elif nav=="L":
        value=plotL
    steps+=1
    print ("nav: ", nav, "value: ", value, "plotL: ", plotL, "plotR: ", plotR)
print(steps)
