from collections import deque
def game(x, y, maps):
    n = len(maps[0])
    m = len(maps)
    if maps[m-1][n-1] == 0:
        return -1

    q = deque()
    q.append((x, y, 1))

    while q:
        x, y, distance = q.popleft()
        if x == n-1 and y == m-1:
            return distance
        
        if maps[y][x] == 0:
            continue
        maps[y][x] = 0

        if x+1 < n:   # right
            q.append((x+1, y, distance+1))
        if x-1 >= 0:  # left
            q.append((x-1, y, distance+1))
        if y+1 < m:   # down
            q.append((x, y+1, distance+1))
        if y-1 >= 0:  # up
            q.append((x, y-1, distance+1))

    return -1


def solution(maps):
    return game(0, 0, maps)