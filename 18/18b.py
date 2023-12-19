from collections import deque


def convert_line(line):
    color_code = line[2][2:-2]
    # convert hex_color to decimal value
    color_code = int(color_code, 16)
    direction = int(line[2][-2:-1])
    dir = ['R', 'D', 'L', 'U']
    dir_str = dir[direction]
    print(dir_str)
    print (color_code)
    return([dir_str, color_code])


def flood_fill(grid, start_x, start_y, max_x, max_y ):
    print("Start flood fill")
    """
    Fills a contiguous area in a 2D grid bounded by a specific color.

    :param grid: 2D grid represented as a list of lists.
    :param start_x: X-coordinate of the starting point.
    :param start_y: Y-coordinate of the starting point.
    :param boundary_color: Color/value representing the boundary.
    :param fill_color: Color/value to fill the area with.
    """
    if grid[start_y][start_x] == '#':
        return
    queue = deque([(start_y, start_x)])
    while queue:
        y, x = queue.popleft()
        if grid[y][x] != '#':
            grid[y][x] = '#'
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if new_x > 0 and new_x < max_x and new_y > 0 and new_y < max_y:
                    queue.append((new_y, new_x))


def get_max_coordinates(digplan):
    max_x = 1
    max_y = 1
    min_x = 1
    min_y = 1
    current_x = 1
    current_y = 1
    for line in digplan:
        direction = line[0]
        steps = int(line[1])
        if direction == "R":
            current_x += steps
        elif direction == "L":
            current_x -= steps
        elif direction == "U":
            current_y -= steps
        elif direction == "D":
            current_y += steps
        if current_x > max_x:
            max_x = current_x
        if current_y > max_y:
            max_y = current_y
        if current_x < min_x:
            min_x = current_x
        if current_y < min_y:
            min_y = current_y
    max_x -= min_x
    max_y -= min_y
    return max_x+3, max_y+3, -min_x+1, -min_y+1


def print_digplan(digplan, grid, offset_x=0, offset_y=0):
    print("Start print_digplan")
    current_x = offset_x+1
    current_y = offset_y+1
    for line in digplan:
        direction = line[0]
        steps = int(line[1])
        if direction == "R":
            # set all grid points to "#" from current_x to current_x + steps
            for i in range(current_x, current_x + steps):
                grid[current_y][i] = "#"
            current_x += steps
        elif direction == "L":
            # set all grid points to "#" from current_x to current_x - steps
            for i in range(current_x, current_x - steps, -1):
                grid[current_y][i] = "#"
            current_x -= steps
        elif direction == "U":
            # set all grid points to "#" from current_y to current_y - steps
            for i in range(current_y, current_y - steps, -1):
                grid[i][current_x] = "#"
            current_y -= steps
        elif direction == "D":
            # set all grid points to "#" from current_y to current_y + steps
            for i in range(current_y, current_y + steps):
                grid[i][current_x] = "#"
            current_y += steps


def count_walls(grid, y, from_x, to_x):
    counter = 0
    wall = False
    for i in range(from_x, to_x):
        if grid[y][i] == "#" and not wall:
            counter += 1
            wall = True
        elif grid[y][i] != "#":
            wall = False
    return counter

# function to fill the area, surrounded by the path, with "#"
def fill_area(grid, max_x, max_y):
    new_grid=grid.copy()
    for y in range(max_y):
        for x in range(max_x):
            if grid[y][x] == ".":
                counter_right = count_walls(grid, y, x, max_x)                
                counter_left = count_walls(grid, y, 0, x)
                if counter_right%2 == 1 and counter_left%2 == 1:
                    new_grid[y][x] = "#"

    return new_grid





digplan = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        line = convert_line(line)
        digplan.append(line)



max_x, max_y, offset_x, offset_y = get_max_coordinates(digplan)
print ("max_x: ", max_x, " max_y: ", max_y, " offset_x: ", offset_x, " offset_y: ", offset_y)
print ("create grid")
exit(0)
grid = [['.' for _ in range(max_x)] for _ in range(max_y)]
print_digplan(digplan, grid, offset_x, offset_y)
for line in grid:
    print(''.join(line))
flood_fill(grid, offset_x+2, offset_y+2, max_x, max_y)
print()
for line in grid:
    print(''.join(line))

# count the number of "#" in the grid
counter = 0
for line in grid:
    counter += line.count("#")
print(counter)


