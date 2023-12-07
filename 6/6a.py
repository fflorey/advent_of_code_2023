
time_list = []
distance_list = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    time_line = lines[0].strip().split()
    distance_line = lines[1].strip().split()

    time_list = [int(time) for time in time_line[1:]]
    distance_list = [int(distance) for distance in distance_line[1:]]

print(time_list)
print(distance_list)

total=1
for i in range(len(time_list)):
    result=[]
    # print("Time:", time_list[i], "Distance:", distance_list[i])
    time=time_list[i]
    distance=distance_list[i]
    for t in range(time):
        speed = t
        distance = speed * (time-t)
        if ( distance > distance_list[i] ):
            # print("Found with speed:", speed)
            result.append(speed)            
    # print ("Result:", result)
    total *= len(result)

# print(result)
print(total)