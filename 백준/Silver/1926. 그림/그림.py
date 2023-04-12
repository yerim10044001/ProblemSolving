import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    area = 1
    q = deque([[x, y]])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]

            if 0 <= x < n and 0 <= y < m and dohwagi[x][y] == 1:
                dohwagi[x][y] = 0
                area += 1
                q.append([x, y])

    return area

if __name__ == "__main__":
    n, m = map(int, input().split())

    dohwagi = [ list(map(int, input().split())) for _ in range(n) ]
    maxArea = 0
    paintCnt = 0
    for i in range(n):
        for j in range(m):
            if dohwagi[i][j] == 1:
                dohwagi[i][j] = 0
                paintCnt += 1
                maxArea = max(maxArea, bfs(i, j))

    print(paintCnt)
    print(maxArea)