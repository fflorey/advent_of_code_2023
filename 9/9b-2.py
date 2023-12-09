file_path = "input.txt"
lines = []

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        integers = [int(num) for num in line.split()]
        lines.append(integers)


result=0
for line in lines:
    differences = []
    differences.append(line)
    while True:
        current_differences = []
        for i in range(1,len(line)):
            difference = line[i] - line[i-1]
            current_differences.append(difference)
        if all(element == 0 for element in current_differences):
            break
        line = current_differences
        differences.append(current_differences)
    nextValue = 0
    for diff in differences[::-1]:  
        nextValue = diff[0] - nextValue
    result+=nextValue    
    
print("Result: ", result)