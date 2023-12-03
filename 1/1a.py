import re

lines = []
with open("input.txt", "r") as file:
    lines = file.readlines()

total_sum = 0
for line in lines:
    numbers = re.findall(r'\d', line)
    print(numbers)
    if numbers:
        first_number = int(numbers[0])
        last_number = int(numbers[-1])
        print(first_number, last_number)
        total_sum += (first_number *10 + last_number)

print(total_sum)


