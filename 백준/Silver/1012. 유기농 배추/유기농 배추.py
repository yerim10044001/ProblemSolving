import sys
input = sys.stdin.readline
from collections import deque


def getGirungi(m, n, k):
    farm = [ [0]*m for _ in range(n) ]
    
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    def bfs(i, j):
        q = deque([[i, j]])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        while q:
            curr = q.popleft()
            
            for i in range(4):
                x = curr[0] + dx[i]
                y = curr[1] + dy[i]
                if 0 <= x < n and 0 <= y < m and farm[x][y] == 1:
                    farm[x][y] = 0
                    q.append([x, y])

    cnt = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                farm[i][j] = 0
                cnt += 1
                bfs(i, j)

    return cnt


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())

        print(getGirungi(m, n, k))
