grid = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            grid.append([int(num) for num in line])

def find_min_heat_loss(grid):
    rows, cols = len(grid), len(grid[0])
    min_loss = float('inf')
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    visited = set()  # To track visited positions with direction and step count

    def find_best_way(row, col, cost, visited):
        nonlocal min_loss
        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited:
            return
        if row == rows - 1 and col == cols - 1:
            min_loss = min(min_loss, cost)
            print("Found! with min_loss = ", min_loss, "cost = ", cost, "row = ", row, "col = ", col)
            return
        visited.add((row, col))
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols:
                find_best_way(new_row, new_col, cost + grid[new_row][new_col], visited)

    find_best_way(0, 0, grid[0][0], visited)
    return min_loss


print(find_min_heat_loss(grid))
