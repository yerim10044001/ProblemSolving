from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)   

    # bfs, find lever
    q = deque()
    q.append((start[0], start[1], 0))
    visited = set()
    visited.add(start)
    lever = (-1, -1)
    while q:
        x, y, cnt = q.popleft()
        if maps[x][y] == 'L':
            lever = (x, y)
            answer += cnt
            break
        for i, j in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            next_x = x+i
            next_y = y+j
            if 0 <= next_x < n and 0 <= next_y < m:
                if (next_x, next_y) not in visited and maps[next_x][next_y] != 'X':
                    visited.add((next_x, next_y))
                    q.append((next_x, next_y, cnt+1))
    if lever[0] == -1:
        return -1
            
    # bfs, find exit
    q = deque()
    q.append((lever[0], lever[1], 0))
    visited = set()
    visited.add(lever)
    exit = (-1, -1)
    while q:
        x, y, cnt = q.popleft()
        if maps[x][y] == 'E':
            exit = (x, y)
            answer += cnt
            break
        for i, j in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            next_x = x+i
            next_y = y+j
            if 0 <= next_x < n and 0 <= next_y < m:
                if (next_x, next_y) not in visited and maps[next_x][next_y] != 'X':
                    visited.add((next_x, next_y))
                    q.append((next_x, next_y, cnt+1))
    if exit[0] == -1:
        return -1
    
    return answer