import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1

    return cnt

if __name__ == "__main__":
    n = int(input())
    graph = [ list(input().rstrip()) for _ in range (n) ]
    visited = [ [False]*n for _ in range(n) ]

    result = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1' and not visited[i][j]:
                result.append(bfs((i, j), visited))
    
    result.sort()
    print(len(result))
    for _ in result: print(_)