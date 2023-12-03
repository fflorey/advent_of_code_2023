
lines = []
with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())

print(lines)
MAXLINES=len(lines)


def process_line(line):
    result = []
    for i, char in enumerate(line):
        if char != '.' and not char.isdigit():
            result.append((i, char))
    return result

def process_lines(lines):
    result = dict()
    n = 0
    for line in lines:
        result[n] = process_line(line)
        n += 1
    return result


def read_numbers(line):
    result = []
    current_number = ""
    for i, char in enumerate(line):
        if char.isdigit():
            current_number += char
        elif current_number:
            result.append((i - len(current_number), int(current_number)))
            current_number = ""
    if current_number:
        result.append((len(line) - len(current_number), int(current_number) ))
    return result

def read_numbers_from_all_lines(lines):
    result = dict()
    n = 0
    for line in lines:
        result[n] = read_numbers(line)
        n += 1
    return result

all_symbols = process_lines(lines)
all_numbers = read_numbers_from_all_lines(lines)

print(all_symbols)
print(all_numbers)

# 20 minutes up to here
found_result=[]
for line, numbers in all_numbers.items():
    for number in numbers:
        x=number[0]
        y=line
        curent_number=number[1]
        print("check for", x,y,curent_number, "MAXLINES",MAXLINES)
        # check if there is any symbol "around" the number
        for cline in range(y-1,y+2):   
            if cline >= 0 and cline <= MAXLINES:
                print("checking line",cline)
                # convert current number to string
                for cnumber in range(x-1,x+len(str(curent_number))+1):
                    print("checking x-xpos",cnumber, "in line:",cline)
                    if cline in all_symbols:
                        print("found line for symbols",cline)
                        for cchar in all_symbols[cline]:
                            print("checking char",cchar)
                            if cchar[0] == cnumber:
                                print("FOUND char",cchar)
                                found_result.append(curent_number)

print(found_result)        
print(sum(found_result))

