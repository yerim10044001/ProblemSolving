import sys
input = sys.stdin.readline
from collections import deque

def BFS(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True

    o, v = 0, 0 # 양, 늑대

    while que:
        i, j = que.popleft()
        
        # sheep or wolf
        if field[i][j] == 'o':
            o += 1
        elif field[i][j] == 'v':
            v += 1

        # next point
        # left
        if i != 0 and not visited[i-1][j] and field[i-1][j] != '#':
            visited[i-1][j] = True
            que.append((i-1, j))
        # right
        if i != r-1 and not visited[i+1][j] and field[i+1][j] != '#':
            visited[i+1][j] = True
            que.append((i+1, j))
        # up
        if j != 0 and not visited[i][j-1] and field[i][j-1] != '#':
            visited[i][j-1] = True
            que.append((i, j-1))
        # down
        if j != c-1 and not visited[i][j+1] and field[i][j+1] != '#':
            visited[i][j+1] = True
            que.append((i, j+1))
    
    if o > v:
        return o, 0
    else:
        return 0, v

if __name__ == "__main__":
    r, c = map(int, input().split())

    field = []
    visited = []
    for _ in range(r):
        field.append(list(input().rstrip()))
        visited.append([False]*c)

    # BFS
    sheep, wolf = 0, 0
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and field[i][j] != '#':
                o, v = BFS(i, j)
                sheep += o
                wolf += v

    print(sheep, wolf)
