def solution(board, h, w):
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    answer = 0
        
    for i in range(4):
        x = h+dx[i]
        y = w+dy[i]
        if 0 <= x < len(board) and 0 <= y <len(board[0]):
            if board[x][y] == board[h][w]:
                answer += 1

    return answer