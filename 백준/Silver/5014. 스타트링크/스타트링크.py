import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    que = deque()
    que.append([s, 0])
    visited[s] = True

    while que:
        q = que.popleft()
        if q[0] == g:   # 도착
            return q[1]

        if q[0] + u <= f and not visited[q[0]+u]:   # 올라가기 가능
            visited[q[0]+u] = True
            que.append([q[0]+u, q[1]+1])
        if q[0] - d >= 1 and not visited[q[0]-d]:   # 내려가기 가능
            visited[q[0]-d] = True
            que.append([q[0]-d, q[1]+1])
    
    return "use the stairs"

if __name__ == "__main__":
    f, s, g, u, d = map(int, input().split())

    visited = [False]*(f+1)
    print(BFS())
