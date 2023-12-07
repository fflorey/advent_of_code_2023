
time_values = []
distance_values = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    time_line = lines[0].strip().split()
    distance_line = lines[1].strip().split()

    time_values = [int(value) for value in time_line[1:]]
    distance_values = [int(value) for value in distance_line[1:]]

print("Time values:", time_values)
print("Distance values:", distance_values)
