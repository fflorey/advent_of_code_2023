import re

def replace_numbers(line):
    numberStr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i in range(len(numberStr)):
        line = line.replace(numberStr[i], numberStr[i][0]+ digits[i] + numberStr[i])
    
    return line

lines = []
with open("input.txt", "r") as file:
    lines = file.readlines()


total_sum = 0
for i in range(len(lines)):
    lines[i] = replace_numbers(lines[i])
    lines[i] = lines[i].strip()
    print(lines[i])
    numbers = re.findall(r'\d', lines[i])
    print(numbers)
    total_sum += (int(numbers[0]) *10 + int(numbers[-1]))

print(total_sum)

total_sum = 0


