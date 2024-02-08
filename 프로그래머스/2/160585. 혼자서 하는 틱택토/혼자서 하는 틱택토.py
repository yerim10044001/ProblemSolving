def solution(board):    
    # 선공과 후공의 개수 비교
    o_cnt = sum(row.count('O') for row in board)
    x_cnt = sum(row.count('X') for row in board)
    if o_cnt == x_cnt or o_cnt-x_cnt == 1:
        pass
    else:
        return 0
    
    # 이미 게임이 종료되었음에도 게임을 진행하였는지 확인
    o_win = False
    x_win = False
    # 가로
    for i in range(3):
        if board[i] == "OOO":
            o_win = True
        if board[i] == "XXX":
            x_win = True
    # 세로
    for i in range(3):
        if board[0][i]+board[1][i]+board[2][i] == "OOO":
            o_win = True
        if board[0][i]+board[1][i]+board[2][i] == "XXX":
            x_win = True
    # 대각선
    if board[0][0]+board[1][1]+board[2][2] == "OOO":
        o_win = True
    if board[0][0]+board[1][1]+board[2][2] == "XXX":
        x_win = True
    if board[0][2]+board[1][1]+board[2][0] == "OOO":
        o_win = True
    if board[0][2]+board[1][1]+board[2][0] == "XXX":
        x_win = True
    
    if o_win and x_win:
        return 0
    if o_win and o_cnt != x_cnt+1:
        return 0
    if x_win and o_cnt != x_cnt:
        return 0

    return 1