
file_path = "input.txt"
lines = []

with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip())



winning_numbers = []
existing_numbers = []

total_points = 0
for line in lines:
    result=[]
    line = line.split(":")[1].strip()
    win= line.split("|")[0].strip().split(" ")
    # remove all empty strings
    win = list(filter(None, win))
    # print(win)
    existing = line.split("|")[1].strip().split(" ")
    # remove all empty strings
    existing = list(filter(None, existing))
    # print(existing)
    # check if any number in existing is in win
    for number1 in existing:
        for number2 in win:
            if number1 == number2:
                result.append(number1)
    print (result)
    if len(result) > 0:
        total_points += 2**(len(result)-1)
        

print(total_points)
print(existing_numbers)


