import sys
input = sys.stdin.readline
from collections import deque

def bfs(startNode, visited):
    q = deque()
    q.append(startNode)
    visited[startNode] = True
    count = 1

    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                count += 1
                visited[w] = True
    return count

if __name__ == "__main__":
    n, m = map(int, input().split())

    # make graph
    graph = [[] for _ in range(0, n+1)]

    for _ in range(0, m):
        v1, v2 = map(int, input().split())
        graph[v2].append(v1)

    # bfs
    maxCnt = 0
    maxList = []
    for i in range(1, n+1):
        cnt = bfs(i, [False]*(n+1))

        if cnt > maxCnt:
            maxCnt = cnt
            maxList = [i]
        elif cnt == maxCnt:
            maxList.append(i)

    for i in maxList:
        print(i, end= ' ')