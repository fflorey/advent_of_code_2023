lines = []
transformation = dict()
counter=0
with open("input.txt", "r") as file:
    # first line are the initial "seed" values
    first_line = file.readline().strip()
    seeds_tmp = first_line.split(":")[1].strip().split(" ")
    seeds_tmp = [int(x) for x in seeds_tmp]
    seeds=[]
    for i in range(0,len(seeds_tmp),2):
        seeds.append([seeds_tmp[i],seeds_tmp[i]+seeds_tmp[i+1]-1])
    print("Seeds:", seeds)

    for line in file:
#        print("Line:", line)
        line = line.strip()
        if not line:
            # line is empty
            continue
        if line and any(char.isalpha() for char in line):
            # line contains a letter
            if not lines:
                continue
#            print(lines)
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
    print("NEXT SEED!\n\n")
    print(seed)
    for key in transformation:
        print(key, transformation[key])
        for dest, source, value in transformation[key]:
            delta=dest-source
            top_border=source+value-1
            print("D", dest, "S", source, "V", value, "seed", seed, source+value)
            bottom=seed[0]
            top=seed[1]
            print("bottom", bottom, "top", top)
            print("source+value", source+value)
            if top < source:
                print("FOUND: low, out")
                continue
            if bottom > top_border:
                print("FOUND: out up")
                continue
            if bottom < source and top >= top_border:
                print("FOUND fat thing, split in three - delta:", delta)
                seed[0] = dest
                seed[1] = dest+value-1
                print("seed is now", seed)
                # new seed for the rest of the range (top)
                seeds.append([source+value, top])
                print("new seed", [source+value, top])
                # new seed for the rest of the range (bottom)
                seeds.append([bottom, source-1])
                print("new seed", [bottom, source-1])
                break
            elif bottom >= source and top < source+value:
                print("FOUND: all in, simply add delta",delta)
                seed[0] = bottom+delta
                seed[1] = top+deltqwqa
                print("seed is now", seed)
                break
            elif bottom >= source and top >= source+value:
                print("FOUND: bottom in, top out, lower bottom, upper top - delta: ", delta)
                seed[0] = bottom+delta
                seed[1] = source+value-1+delta
                print("seed is now", seed)
                # new seed for the rest of the range (top)
                seeds.append([source+value, top])
                print("new seed", [source+value, top])
                break
            elif bottom < source and top <= source+value:
                print("FOUND: bottom out, top in, upper top - delta:", delta)
                seed[0] = source+delta
                seed[1] = top+delta
                print("seed is now", seed)
                seeds.append([bottom, source-1])
                print("new seed", [bottom, source-1])
                break
        print("seed", seed)
        print("seeds", seeds)
        # read = input("Press enter to continue")
    result.append(seed)

print("Result:", seeds)
print("Result:", result)

print ("lowest number in result: ", min(result))