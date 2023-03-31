import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, startNode):
    q = deque()
    q.append(startNode)
    visited = [False]*(n+1)
    visited[startNode] = True

    while q:
        node = q.popleft()
        print(node, end=' ')
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

def dfs(n, startNode):
    visited = [False]*(n+1)
    visited[startNode] = True
    def recur(node):
        print(node, end=' ')
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                recur(v)
    recur(startNode)

if __name__ == "__main__":
    n, m, s = map(int, input().split())
    graph = {}

    for i in range(1, n+1):
        graph[i] = []

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for i in range(1, n+1):
        graph[i].sort()

    dfs(n, s)
    print()
    bfs(n, s)