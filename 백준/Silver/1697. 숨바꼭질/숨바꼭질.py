import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001

def bfs(n, k):
    q = deque([n])
    visited = [0]*MAX

    while q:
        x = q.popleft()

        if x == k: return visited[x]

        for i in [x+1, x-1, 2*x]:
            if 0 <= i < MAX and visited[i] == 0:
                visited[i] = visited[x]+1
                q.append(i)

    return -1


if __name__ == "__main__":
    n, k = map(int, input().split())

    print(bfs(n, k))