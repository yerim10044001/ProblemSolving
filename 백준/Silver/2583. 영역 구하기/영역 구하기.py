import sys
input = sys.stdin.readline
from collections import deque

def bfs(y, x):
    q = deque([[y, x]])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1
    while q:
        y, x = q.popleft()

        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0 <= a < n and 0 <= b < m and monunjongi[b][a] != 1:
                q.append([b, a])
                monunjongi[b][a] = 1
                cnt+=1
    return cnt

if __name__ == "__main__":
    m, n, k = map(int, input().split())

    monunjongi = [ [0]*n for _ in range(m) ]
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                monunjongi[i][j] = 1
    
    result = []
    for i in range(m):
        for j in range(n):
            if monunjongi[i][j] != 1:
                monunjongi[i][j] = 1
                result.append(bfs(i, j))

    result.sort()
    result = list(map(str, result))
    print(len(result))
    print(' '.join(result))