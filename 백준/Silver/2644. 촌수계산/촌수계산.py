import sys
from collections import deque
input = sys.stdin.readline

def dfs(node, cnt):
    if node == y:
        global result
        result = cnt
    
    for v in graph[node]:
        if not visited[v]:
            visited[v] = True
            dfs(v, cnt+1)


if __name__ == "__main__":
    n = int(input())
    x, y = map(int, input().split())
    m = int(input())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        p, s = map(int, input().split())
        graph[p].append(s)
        graph[s].append(p)

    visited = [False] * (n+1)
    visited[x] = True
    result = -1
    dfs(x, 0)

    print(result)
