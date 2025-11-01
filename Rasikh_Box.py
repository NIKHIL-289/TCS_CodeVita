n, m = map(int, input().split())
grid = [input().split() for _ in range(n)]

k = int(input("Enter the number of movement: "))
direction = input("Enter the direction of movement: ").strip().lower()

def right_move(g):
    return [list(row) for row in zip(*g[::-1])]

def left_move(g):
    return [list(row) for row in zip(*g)][::-1]

def gravity(g):
    n, m = len(g), len(g[0])
    for j in range(m):
        col = [g[i][j] for i in range(n)]
        stars = col.count('*')
        for i in range(n):
            g[i][j] = '.' if i < n - stars else '*'
    return g

k %= 4
if direction == "left":
    for _ in range(k):
        grid = left_move(grid)
else:
    for _ in range(k):
        grid = right_move(grid)

grid = gravity(grid)

for row in grid:
    print(' '.join(row))