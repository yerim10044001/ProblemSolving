from collections import deque
def solution(maps):
    def dfs(start):
        days = 0
        q = deque()
        q.append([start[0], start[1]])

        while q:
            x, y = q.pop()
            days += int(maps[x][y])
            for i, j in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                if 0<=x+i<n and 0<=y+j<m and not visited[x+i][y+j]:
                    if maps[x+i][y+j] != 'X':
                        q.append([x+i, y+j])
                    visited[x+i][y+j] = True
        return days
    
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
        
    for i in range(n):
        for j in range(m):          
            if maps[i][j] != 'X' and not visited[i][j]:   
                visited[i][j] = True
                answer.append(dfs([i, j]))
            visited[i][j] = True
    if len(answer) == 0:
        return [-1]
    return sorted(answer)