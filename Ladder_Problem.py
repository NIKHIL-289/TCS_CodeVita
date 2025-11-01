from collections import deque

m, n = map(int, input().split())
g = [list(input().strip()) for _ in range(m)]

src = [(i,j) for i in range(m) for j in range(n) if g[i][j]=='l']
dst = [(i,j) for i in range(m) for j in range(n) if g[i][j]=='L']

def orient(c): return 'h' if c[0][0]==c[1][0] else 'v'
def mid(c): return c[len(c)//2]

start = (mid(src)[0], mid(src)[1], orient(src))
goal  = (mid(dst)[0], mid(dst)[1], orient(dst))

def free(x,y): return 0<=x<m and 0<=y<n and g[x][y]!='B'

def can_move(x,y,o,dx,dy):
    if o=='h':
        cells=[(x,y-1+dy),(x,y+dy),(x,y+1+dy)]
        return all(free(x+dx,c) for c in range(y-1,y+2)) if dx else all(free(x,y+dy+i) for i in (-1,0,1))
    else:
        cells=[(x-1+dx,y),(x+dx,y),(x+1+dx,y)]
        return all(free(r,y+dy) for r in range(x-1,x+2)) if dy else all(free(x+dx+i,y) for i in (-1,0,1))

def can_rot(x,y,o):
    for i in (-1,0,1):
        for j in (-1,0,1):
            if not free(x+i,y+j): return False
    return True

q = deque([(start,0)])
vis = {start}

while q:
    (x,y,o),d = q.popleft()
    if (x,y,o)==goal: print(d); break
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if can_move(x,y,o,dx,dy):
            s=(x+dx,y+dy,o)
            if s not in vis: vis.add(s); q.append((s,d+1))
    if can_rot(x,y,o):
        no = 'v' if o=='h' else 'h'
        s=(x,y,no)
        if s not in vis: vis.add(s); q.append((s,d+1))
else:
    print("Impossible")
