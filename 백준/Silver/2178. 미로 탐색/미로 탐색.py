import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m):
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque()
    q.append((0, 0, 1))

    while q:
        x, y, cnt = q.popleft()

        # arrive at (N, M)
        if x == n-1 and y == m-1:
            return cnt

        # left
        if y > 0 and miro[x][y-1] == '1' and not visited[x][y-1]:
            visited[x][y-1] = True
            q.append((x, y-1, cnt+1))
        # right
        if y < m-1 and miro[x][y+1] == '1' and not visited[x][y+1]:
            visited[x][y+1] = True
            q.append((x, y+1, cnt+1))
        # up
        if x > 0 and miro[x-1][y] == '1' and not visited[x-1][y]:
            visited[x-1][y] = True
            q.append((x-1, y, cnt+1))
        # down
        if x < n-1 and miro[x+1][y] == '1' and not visited[x+1][y]:
            visited[x+1][y] = True
            q.append((x+1, y, cnt+1))


if __name__ == "__main__":
    n, m = map(int, input().split())

    miro = [ list(input().rstrip()) for _ in range(n) ]
    print(bfs(n, m))
    