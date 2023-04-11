import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    n = int(input())
    r1, c1, r2, c2 = map(int, input().split())

    q = deque([[r1, c1]])
    visited = [ [-1]*n for _ in range(n) ]
    visited[r1][c1] = 0

    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]

    while q:
        r, c = q.popleft()

        if r == r2 and c == c2:
            print(visited[r][c])
            exit(0)
        
        for i in range(6):
            x = r+dx[i]
            y = c+dy[i]

            if 0 <= x < n and 0 <= y < n and visited[x][y] == -1:
                visited[x][y] = visited[r][c]+1
                q.append([x, y])

    print(-1)
