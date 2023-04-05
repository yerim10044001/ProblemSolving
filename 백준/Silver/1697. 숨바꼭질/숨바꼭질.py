import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, k):
    q = deque()
    q.append([n, 0])
    visited = set()
    visited.add(n)

    while q:
        x, t = q.popleft()

        if x == k: return t

        for i in [x+1, x-1, 2*x]:
            if 0 <= i <= 100000 and i not in visited:
                visited.add(i)
                q.append([i, t+1])

    return -1


if __name__ == "__main__":
    n, k = map(int, input().split())

    print(bfs(n, k))