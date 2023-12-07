import math

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
# for i in range(len(time_list)):
#     result=0
#     # print("Time:", time_list[i], "Distance:", distance_list[i])
#     time=time_list[i]
#     distance=distance_list[i]
#     for t in range(time):
#         distance = t * (time-t)
#         if ( distance > distance_list[i] ):
#             # print("Found with speed:", speed)
#             result+=1
#     # print ("Result:", result)
#     total *= result

print("2nd way")
total=1
for i in range(len(time_list)):
    x = time_list[i]
    D = distance_list[i]
    s1 = x/2 + math.sqrt(x*x/4 - D)
    s2 = x/2 - math.sqrt(x*x/4 - D)
    f1=math.ceil(s1)
    f2=math.floor(s2)+1
    print("s1", s1, "s2", s2)
    print("f1", f1, "f2", f2)
    total *= (f1-f2)

print(f1-f2)
print(total)