import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()

    # add redTomatoes in queue
    for i in range(h):
        for j in range(n):
            for k in range(m):
               if tomatoBoxes[i][j][k] == 1:
                   q.append([i, j, k, 0])
    
    maxDate = 0

    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while q:
        z, y, x, date = q.popleft()
        maxDate = max(maxDate, date)

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if tomatoBoxes[nz][ny][nx] == 0:
                    tomatoBoxes[nz][ny][nx] = 1
                    q.append([nz, ny, nx, date+1])

    # get result
    for i in range(h):
        for j in range(n):
            if tomatoBoxes[i][j].count(0) != 0: return -1
    else: return maxDate
    


if __name__ == "__main__":
    m, n, h = map(int,input().split())

    # get tomato
    tomatoBoxes = []
    for i in range(h):
        oneBox = []
        for _ in range(n):
            oneBox.append(list(map(int, input().split())))
        tomatoBoxes.append(oneBox)

    print(bfs())

