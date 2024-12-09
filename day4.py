def sol1(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def find_word(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]: 
                for dx, dy in directions:
                    if find_word(i, j, dx, dy):
                        count += 1
    return count


def sol2(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    def is_x_mas(x, y):
        if not (0 <= x - 1 < rows and 0 <= x + 1 < rows and
                0 <= y - 1 < cols and 0 <= y + 1 < cols):
            return False
        diagonal1 = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1]
        diagonal2 = grid[x - 1][y + 1] + grid[x][y] + grid[x + 1][y - 1]
        return (diagonal1 == "MAS" or diagonal1 == "SAM") and \
               (diagonal2 == "MAS" or diagonal2 == "SAM")
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == "A" and is_x_mas(i, j):
                count += 1

    return count

f = open('day4.txt','r')
g =[elem.replace('\n','') for elem in f]
print(sol1(g), sol2(g))