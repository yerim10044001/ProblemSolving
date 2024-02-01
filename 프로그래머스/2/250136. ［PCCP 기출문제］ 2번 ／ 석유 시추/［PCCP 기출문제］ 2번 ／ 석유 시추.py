from collections import deque

def solution(land):
    

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    row_list = [0 for _ in range(len(land[0]))]
    q = deque()
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            
            if land[i][j] == 1:
                row_check = set()
                oil = 0
                
                # dfs
                q.append([i, j])
                row_check.add(j)
                oil += 1
                land[i][j] = 0
                
                while q:
                    x, y = q.pop()

                    for k in range(4):
                        xx = x+dx[k]
                        yy = y+dy[k]
                        if 0 <= xx < len(land) and 0 <= yy < len(land[0]) and land[xx][yy]==1:
                            q.append([xx, yy])  
                            row_check.add(yy)
                            land[xx][yy] = 0
                            oil += 1
                                
                # oil
                for r in row_check:
                    row_list[r] += oil
    

    max_oil = max(row_list)
    
    return max_oil