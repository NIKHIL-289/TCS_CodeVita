def read_input():
    N = int(input())
    segments = [tuple(map(int, input().split())) for _ in range(N)]
    return segments

def build_grid(segments):
    grid = [[0 for _ in range(26)] for _ in range(26)]
    for x1, y1, x2, y2 in segments:
        grid[y1][x1] = 1
        grid[y2][x2] = 1
    return grid

def find_squares(grid):
    squares = []
    for y in range(25):
        for x in range(25):
            if grid[y][x] and grid[y][x+1] and grid[y+1][x] and grid[y+1][x+1]:
                squares.append((x, y))
    return squares

def are_squares_connected(squares):
    """Check if all squares form one connected group (simple DFS)."""
    if not squares:
        return False
    visited = set()
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    def dfs(x, y):
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if (nx, ny) in squares and (nx, ny) not in visited:
                visited.add((nx, ny))
                dfs(nx, ny)

    first = squares[0]
    visited.add(first)
    dfs(*first)
    return len(visited) == len(squares)

def is_possible_cube_net(squares):
    """Simplified check: must be 6 connected equal squares."""
    if len(squares) != 6:
        return False
    return are_squares_connected(squares)

def calculate_volume(segments):
    grid = build_grid(segments)
    squares = find_squares(grid)
    if is_possible_cube_net(squares):
        side = 1  # unit side assumed
        return side ** 3
    else:
        return 0

# ---------------- MAIN ----------------
if __name__ == "__main__":
    segments = read_input()
    result = calculate_volume(segments)
    print(result)
