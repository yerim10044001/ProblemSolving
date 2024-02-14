from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)   
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
                
    # bfs
    def bfs(start, end):
        answer = 0
        q = deque()
        q.append((start[0], start[1], 0))
        visited = set()
        visited.add(start)
        while q:
            x, y, cnt = q.popleft()
            if x == end[0] and y == end[1]:
                return cnt
            for i, j in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                next_x = x+i
                next_y = y+j
                if 0 <= next_x < n and 0 <= next_y < m:
                    if (next_x, next_y) not in visited and maps[next_x][next_y] != 'X':
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y, cnt+1))
        return -1
    
    # bfs, find lever
    lever_cnt = bfs(start, lever)
    if lever_cnt == -1:
        return -1
    else: answer += lever_cnt
    
    # bfs, find exit
    exit_cnt = bfs(lever, exit)
    if exit_cnt == -1:
        return -1
    else: answer += exit_cnt
    
    return answer