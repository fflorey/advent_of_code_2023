lines = []
transformation = dict()
counter=0
with open("input.txt", "r") as file:
    # first line are the initial "seed" values
    first_line = file.readline().strip()
    seeds = first_line.split(":")[1].strip().split(" ")
    seeds = [int(x) for x in seeds]
    print(seeds)

    for line in file:
        print("Line:", line)
        line = line.strip()
        if not line:
            # line is empty
            continue
        if line and any(char.isalpha() for char in line):
            # line contains a letter
            if not lines:
                continue
            print(lines)
            transformation[counter] = lines
            lines = []
            counter+=1
        else:
            # line does not contain a letter
            lines.append([int(x) for x in line.strip().split(" ")])  # Append line to lines and convert elements to int

print(lines)
print("LEN:", len(transformation), "COUNTER:", counter, transformation)
print("Seeds:", seeds)

result=[]
for seed in seeds:
    print(seed)
    for key in transformation:
        print(key, transformation[key])
        for dest, source, value in transformation[key]:
            print("D", dest, "S", source, "V", value, "seed", seed, source+value)
            # print("seed >= source", seed >= source, "seed < source+value", seed < source+value)
            if seed >= source and seed < source+value:
                print("Found:", seed, "in", source, value)
                print("Dest:", dest)
                seed += dest-source
                print ("New seed:", seed)
                break
    result.append(seed)

print("Result:", seeds)
print("Result:", result)

print ("lowest nummber in result: ", min(result))