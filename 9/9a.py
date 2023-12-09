file_path = "input.txt"
lines = []

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        integers = [int(num) for num in line.split()]
        lines.append(integers)

def isEveryDifferenceNull(list):
    for element in list:
        if element != 0:
            return False
    return True

result=0
for line in lines:
    print("line: ", line)
    differences = {}
    differences[0] = line
    counter = 1
    while True:
        differences[counter] = []
        previous_value = None  # Add this line to reset previous_value
        for value in line:
            if previous_value is not None:
                difference = value - previous_value
                differences[counter].append(difference)
            previous_value = value
        print(differences[counter])
        if isEveryDifferenceNull(differences[counter]):
            break
        line = differences[counter]
        counter += 1
    print("Differences: ", differences)
    nextValue = 0
    for diffs in differences.values():
        nextValue += diffs[-1]
    print("Next Value: ", nextValue)
    result+=nextValue

    
    
print("Result: ", result)