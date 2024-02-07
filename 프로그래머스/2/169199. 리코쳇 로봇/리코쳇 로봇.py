from collections import deque
def solution(board):
    # i번째 행에서의 D 위치
    d_row = { i:[-1] for i in range(0, len(board))}
    # i번째 열에서의 D 위치
    d_col = { i:[-1] for i in range(0, len(board[0]))}
    
    # find D, R, G
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == 'D':
                d_row[i].append(j)
                d_col[j].append(i)
            elif board[i][j] == 'R':
                r = [i, j]
            elif board[i][j] == 'G':
                g = [i, j]
    for i in range(0, len(board)):
        d_row[i].append(len(board[0]))
    for j in range(0, len(board[0])):
        d_col[j].append(len(board))

    # bfs
    q = deque()
    q.append([r, 0])
    visited = [[False]*len(board[0]) for _ in range(len(board))]
    visited[r[0]][r[1]] = True
    
    while q:
        loc, cnt = q.popleft()
        # 목적지 도착
        if board[loc[0]][loc[1]] == 'G':
            return cnt
        
        # 위
        if loc[0] > 0:
            # 위로 이동가능한 칸 찾기
            for j in d_col[loc[1]]:
                if loc[0] <= j:
                    break
                d_up = j+1
            if not visited[d_up][loc[1]]:
                visited[d_up][loc[1]] = True
                q.append([[d_up, loc[1]], cnt+1])
        # 아래
        if loc[0] < len(board)-1:
            # 아래로 이동가능한 칸 찾기
            for j in reversed(d_col[loc[1]]):
                if loc[0] >= j:
                    break
                d_down = j-1
            if not visited[d_down][loc[1]]:
                visited[d_down][loc[1]] = True
                q.append([[d_down, loc[1]], cnt+1])
        # 왼쪽
        if loc[1] > 0:
            # 왼쪽으로 이동가능한 칸 찾기
            for i in d_row[loc[0]]:
                if loc[1] <= i:
                    break
                d_left = i+1
            if not visited[loc[0]][d_left]:
                visited[loc[0]][d_left] = True
                q.append([[loc[0], d_left], cnt+1])
        # 오른쪽
        if loc[1] < len(board[0])-1:
            # 오른쪽으로 이동가능한 칸 찾기
            for i in reversed(d_row[loc[0]]):
                if loc[1] >= i:
                    break
                d_right = i-1
            if not visited[loc[0]][d_right]:
                visited[loc[0]][d_right] = True
                q.append([[loc[0], d_right], cnt+1])
    
    return -1