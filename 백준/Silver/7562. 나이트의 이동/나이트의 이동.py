import sys
input = sys.stdin.readline
from collections import deque


def bfs(l, start, end):
    chess = [ [0]*l for _ in range(l) ]
    chess[start[0]][start[1]] = 1

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]

    q = deque([start])
    while q:
        night = q.popleft()
        if night[0] == end[0] and night[1] == end[1]:
            break
        
        for i in range(8):
            x = night[0]+dx[i]
            y = night[1]+dy[i]
            if 0 <= x < l and 0 <= y < l and chess[x][y] == 0:
                chess[x][y] = chess[night[0]][night[1]] + 1
                q.append([x, y])


    return chess[end[0]][end[1]]-1


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        l = int(input())
        start = list(map(int, input().split()))
        end = list(map(int, input().split()))

        print(bfs(l, start, end))
