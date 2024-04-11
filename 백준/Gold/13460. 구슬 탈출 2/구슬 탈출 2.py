import sys
from collections import deque
input = sys.stdin.readline


    


def escape(n, m):
    def slide(x, y, dx, dy, other):
        while True:
            if board[x+dx][y+dy] == 'O':
                return x+dx, y+dy
            elif board[x+dx][y+dy] == '#':
                break
            # 빨간공이 움직일 때 파란공 만나거나
            # 파란공이 움직일 때 빨간공 만난 경우
            elif x+dx == other[0] and y+dy == other[1]:
                break
            x += dx
            y += dy
        return [x, y]

    board = [ input().rstrip() for _ in range(n) ]
    redX, redY, blueX, blueY = -1, -1, -1, -1
    # get R, B location
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                redX, redY = i, j
            elif board[i][j] == 'B':
                blueX, blueY = i, j
    
    # game start
    q = deque()
    visited = []
    q.append([[redX, redY], [blueX, blueY], 0])
    visited.append(((redX, redY), (blueX, blueY)))

    while q:
        red, blue, cnt = q.popleft()

        # game over
        if cnt > 10:
            continue
        elif board[blue[0]][blue[1]] == 'O': continue
        elif board[red[0]][red[1]] == 'O': return cnt
        
        # slide balls
        # up
        if blue[0] < red[0]:
            next_blue = slide(blue[0], blue[1], -1, 0, red)
            next_red = slide(red[0], red[1], -1, 0, next_blue)
        else:
            next_red = slide(red[0], red[1], -1, 0, blue)
            next_blue = slide(blue[0], blue[1], -1, 0, next_red)
        if ((next_red[0], next_red[1]), (next_blue[0], next_blue[1])) not in visited:
            visited.append(((next_red[0], next_red[1]), (next_blue[0], next_blue[1])))
            q.append([next_red, next_blue, cnt+1])
        
        # down
        if blue[0] > red[0]:    
            next_blue = slide(blue[0], blue[1], 1, 0, red)
            next_red = slide(red[0], red[1], 1, 0, next_blue)
        else:
            next_red = slide(red[0], red[1], 1, 0, blue)
            next_blue = slide(blue[0], blue[1], 1, 0, next_red)
        if ((next_red[0], next_red[1]), (next_blue[0], next_blue[1])) not in visited:
            visited.append(((next_red[0], next_red[1]), (next_blue[0], next_blue[1])))
            q.append([next_red, next_blue, cnt+1])
        
        # left
        if blue[1] < red[1]:    
            next_blue = slide(blue[0], blue[1], 0, -1, red)
            next_red = slide(red[0], red[1], 0, -1, next_blue)
        else:
            next_red = slide(red[0], red[1], 0, -1, blue)
            next_blue = slide(blue[0], blue[1], 0, -1, next_red)
        if ((next_red[0], next_red[1]), (next_blue[0], next_blue[1])) not in visited:
            visited.append(((next_red[0], next_red[1]), (next_blue[0], next_blue[1])))
            q.append([next_red, next_blue, cnt+1])

        # right
        if blue[1] > red[1]:    
            next_blue = slide(blue[0], blue[1], 0, 1, red)
            next_red = slide(red[0], red[1], 0, 1, next_blue)
        else:
            next_red = slide(red[0], red[1], 0, 1, blue)
            next_blue = slide(blue[0], blue[1], 0, 1, next_red)
        if ((next_red[0], next_red[1]), (next_blue[0], next_blue[1])) not in visited:
            visited.append(((next_red[0], next_red[1]), (next_blue[0], next_blue[1])))
            q.append([next_red, next_blue, cnt+1])
        
    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())

    print(escape(n, m))