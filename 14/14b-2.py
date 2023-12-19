lines = []
with open("./input.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

MAXX = len(lines[0])
MAXY = len(lines)
print(MAXX, MAXY)


# Create a new grid to store the updated positions

for rounds in range(3):
    for cycle in range(4):
        new_lines = [['.' for _ in range(MAXX)] for _ in range(MAXY)]
        for y in range(MAXY):
            for x in range(MAXX):
                if lines[y][x] == '#':
                    new_lines[y][x] = '#'
                if lines[y][x] == 'O':
                    # Move the movable element to the top if the field is empty
                    if y == 0:
                        new_lines[y][x] = 'O'
                    else:
                        for i in range(y-1, -1, -1):
                            new_lines[i+1][x] = '.'                        
                            if new_lines[i][x] == 'O':
                                new_lines[i+1][x] = 'O'
                                break
                            if new_lines[i][x] == '#':
                                new_lines[i+1][x] = 'O'
                                break  
                            elif new_lines[i][x] == '.':
                                new_lines[i][x] = 'O'
                                new_lines[y][x] = '.'                        

                # Print the updated grid


       
        lines=new_lines.copy()
        total=0
        counter=MAXY+1
        for line in lines:
            counter -= 1
            for char in line:
                if char == 'O':
                    total += counter

        print(total)

        for r in range(3):
            lines = list(zip(*new_lines[::-1]))
    print("nach falling")
    for line in new_lines:
        print(''.join(line))







