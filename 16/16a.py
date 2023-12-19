def simulate_beam(grid):
    rows, cols = len(grid), len(grid[0])
    direction = (0, 1)  # Initial direction: right
    energized_tiles = set()
    beams = [(0, 0, direction)]  # Starting position with direction

    while beams:
        print("Beams:", beams)
        new_beams = []
        for row, col, (dr, dc) in beams:
            while 0 <= row < rows and 0 <= col < cols:
                energized_tiles.add((row, col))
                tile = grid[row][col]

                if tile == '/':
                    dr, dc = -dc, -dr  # Change direction for /
                elif tile == '\\':
                    dr, dc = dc, dr  # Change direction for \
                elif tile in ['|', '-']:
                    if (dr == 0 and tile == '|') or (dc == 0 and tile == '-'):
                        # Split the beam
                        new_beams.append((row, col, (dr, -dc)))
                        new_beams.append((row, col, (-dr, dc)))
                        break  # Stop current beam and handle new beams

                row += dr
                col += dc

        beams = new_beams

    return len(energized_tiles)

# Test the revised function with the provided grid
grid = [
    ".|...\\....",
    "|.-.\\.....",
    ".....|-...",
    "........|.",
    "..........",
    ".........\\",
    "..../.\\\\..",
    ".-.-/..|..",
    ".|....-|.|",
    "..//.|...."
]

simulate_beam(grid)
