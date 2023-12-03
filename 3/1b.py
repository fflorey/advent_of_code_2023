
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

# 1h from here
found_result=[]
for line, symbols in all_symbols.items():
    # check for the '*' symbol in the line
    for symbol in symbols:
        tmp_result=[]
        x=symbol[0]
        y=line
        curent_symbol=symbol[1]
        print("check for", x,y,curent_symbol, "MAXLINES",MAXLINES)
        if curent_symbol == '*':
            for cline in range(y-1,y+2):   
                if cline >= 0 and cline <= MAXLINES:
                    print("checking line",cline)
                    # convert current number to string
                    # check if there is any number "around" the symbol
                    for cnumber in all_numbers[cline]:
                        cx=cnumber[0]
                        cy=cline
                        curent_number=cnumber[1]
                        clen=len(str(curent_number))
                        print("check for", cx,cy,curent_number, "with len", clen)
                        if x >= cx-1 and x <= cx+clen:
                            if y >= cy-1 and y <= cy+1:
                                tmp_result.append((cx,cy,curent_number))
                                print("found",cx,cy,curent_number)
                                
        # check if tmp_result has exactly 2 elements
        if len(tmp_result) == 2:            
            print("found_result with 2 entries!",tmp_result)
            # multiply the numbers
            print("result",tmp_result[0][2]*tmp_result[1][2])
            # append the result to the found_result list
            found_result.append(tmp_result[0][2]*tmp_result[1][2])


print(found_result)       
print("final result",sum(found_result)) 

