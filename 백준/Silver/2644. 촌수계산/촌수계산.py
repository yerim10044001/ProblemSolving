import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    q = deque()
    q.append((start, 0))
    visited = [False]*(n+1)
    visited[start] = True
    
    while q:
        node, cnt = q.popleft()

        if node == end:
            return cnt

        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                q.append((v, cnt+1))

    return -1

if __name__ == "__main__":
    n = int(input())
    x, y = map(int, input().split())
    m = int(input())

    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    for _ in range(m):
        p, s = map(int, input().split())
        graph[p].append(s)
        graph[s].append(p)

    print(bfs(x, y))    
