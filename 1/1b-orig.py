import re

lines = []
with open("input.txt", "r") as file:
    lines = file.readlines()

findStrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
replaceStrings = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# replace all the words in the list with the corresponding number, starting from the left side of each line
for i in range(len(lines)):
    pos = 0
    while True:
        pos=9999999
        found = False
        number = -1
        for j in range(len(findStrings)):
            fpos = lines[i].find(findStrings[j])
            if fpos != -1 and fpos < pos:
                found = True
                pos = fpos
                number = j
        
        if found == True:
            lines[i] = lines[i][:pos] + replaceStrings[number] + lines[i][pos+len(findStrings[number]):].strip()            
        else:
            lines[i] = lines[i].strip()
            break   

# print all new lines and remove all spaces and newlines
for line in lines:
    print(line)

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


