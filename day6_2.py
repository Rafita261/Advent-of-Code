def parse_map(input_map):
    """
    Parse the map input into a grid, starting position of the guard, and initial direction.
    """
    grid = [list(line) for line in input_map.strip().split("\n")]
    guard_pos = None
    guard_dir = None

    # Find guard starting position and direction
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in "^>v<":
                guard_pos = (r, c)
                if cell == "^":
                    guard_dir = (-1, 0)  # Up
                elif cell == ">":
                    guard_dir = (0, 1)  # Right
                elif cell == "v":
                    guard_dir = (1, 0)  # Down
                elif cell == "<":
                    guard_dir = (0, -1)  # Left
                grid[r][c] = "."  # Replace guard's starting position with an empty space
                break
        if guard_pos:
            break

    return grid, guard_pos, guard_dir


def move_guard(grid, pos, direction):
    """
    Simulate the guard's movement based on the rules.
    """
    r, c = pos
    dr, dc = direction
    new_pos = (r + dr, c + dc)

    # Check if the new position is within bounds and not an obstacle
    if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]) and grid[new_pos[0]][new_pos[1]] != "#":
        return new_pos, direction  # Move forward
    else:
        # Turn right: clockwise rotation
        if direction == (-1, 0):  # Up
            return pos, (0, 1)  # Right
        elif direction == (0, 1):  # Right
            return pos, (1, 0)  # Down
        elif direction == (1, 0):  # Down
            return pos, (0, -1)  # Left
        elif direction == (0, -1):  # Left
            return pos, (-1, 0)  # Up


def simulate_path(grid, guard_pos, guard_dir):
    """
    Simulate the guard's movement and check if it results in a loop.
    """
    visited = {}
    step = 0

    while guard_pos not in visited:
        visited[guard_pos] = step
        guard_pos, guard_dir = move_guard(grid, guard_pos, guard_dir)
        step += 1
        # Check if the guard leaves the map
        if not (0 <= guard_pos[0] < len(grid) and 0 <= guard_pos[1] < len(grid[0])):
            return False  # Guard leaves the map

    return True  # Guard is in a loop


def find_loop_positions(input_map):
    """
    Find all positions where adding an obstruction would result in the guard being stuck in a loop.
    """
    grid, guard_start_pos, guard_start_dir = parse_map(input_map)
    loop_positions = []

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == '.' and (r, c) != guard_start_pos:
                # Place an obstruction
                grid[r][c] = '#'
                if simulate_path(grid, guard_start_pos, guard_start_dir):
                    loop_positions.append((r, c))
                # Remove the obstruction
                grid[r][c] = '.'

    return loop_positions


# Example input map
input_map = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

# Solve the problem
loop_positions = find_loop_positions(input_map)
print(f"Number of positions to create a loop: {(len(input_map)*len(input_map[0]))-len(loop_positions)}")
