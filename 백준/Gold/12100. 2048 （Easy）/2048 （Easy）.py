import sys
input = sys.stdin.readline

def game2048(n):
    def move(board, cnt, dx, dy):
        if cnt >= 5:
            return max(map(max, board))
        new_board = [ [0]*n for _ in range(n) ]

        if dx != 0:
            if dx == -1: start = n-1
            elif dx == 1: start = 0
            for j in range(n):
                stack = []
                i, prev = start, 0
                while 0 <= i < n:
                    if board[i][j] != 0:
                        if prev == board[i][j]: 
                            stack[-1] *= 2
                            prev = 0
                        else: 
                            stack.append(board[i][j])
                            prev = board[i][j]
                    i += dx
                i = start
                prev = 0
                while stack:
                    new_board[i][j] = stack.pop(0)
                    i += dx
        elif dy != 0:
            if dy == -1: start = n-1
            elif dy == 1: start = 0
            for i in range(n):
                stack = []
                j, prev = start, 0
                while 0 <= j < n:
                    if board[i][j] != 0:
                        if prev == board[i][j]: 
                            stack[-1] *= 2
                            prev = 0
                        else: 
                            stack.append(board[i][j])
                            prev = board[i][j]
                    j += dy
                j = start
                while stack:
                    new_board[i][j] = stack.pop(0)
                    j += dy
        
        # up, down, left, right
        return max(move(new_board, cnt+1, 1, 0),
                   move(new_board, cnt+1, -1, 0),
                   move(new_board, cnt+1, 0, 1),
                   move(new_board, cnt+1, 0, -1))

    board = [ list(map(int, input().split())) for _ in range(n) ]

    return max(move(board, 0, 1, 0),
                move(board, 0, -1, 0),
                move(board, 0, 0, 1),
                move(board, 0, 0, -1))
    

if __name__ == "__main__":

    n = int(input())
    print(game2048(n))