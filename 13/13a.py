def find_max_mirrored_lines(block):
    max_mirrored_lines = 0
    mirrored_line = -1
    for i in range(len(block) - 1):
        if block[i] == block[i+1]:
            count = 0         
            while i-count >= 0 and i+count+1 < len(block) and block[i-count] == block[i+count+1]:
                count += 1
            if count > max_mirrored_lines and (len(block) == i+count+1 or i+1-count == 0):
                mirrored_line = i
                max_mirrored_lines = count

    if (mirrored_line == -1):
        return -1, -1
    return max_mirrored_lines, mirrored_line+1

def printBlock(block):
    for line in block:
        print(line)

def checkBlock(block):
    nlines, max1 = find_max_mirrored_lines(block)
    # rotate block by 90 degrees
    block = list(zip(*block[::-1]))
    nlines, max2 = find_max_mirrored_lines(block)
    if max1 > max2:
        return max1*100
    else:
        return max2
    

def read_blocks_from_file(file_path):
    global total
    blocks = []
    block_nr = 0 
    current_block = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                current_block.append(tuple(line))
            elif current_block:
                print("Block", block_nr, "has", checkBlock(current_block), "points")
                block_nr += 1
                blocks.append(current_block)
                total += checkBlock(current_block)
                current_block = []

        if current_block:
            print("Block", block_nr, "has", checkBlock(current_block), "points")
            block_nr += 1
            blocks.append(current_block)
            total += checkBlock(current_block)

    return blocks

total = 0
file_path = "input.txt"
blocks = read_blocks_from_file(file_path)
print("Total:", total)