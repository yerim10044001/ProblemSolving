import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    R, C = map(int, input().split())
    miro = []
    q = deque()

    for r in range(R):
        miro.append(list(input().rstrip()))

        # find Fire and Jihoon's location
        for c in range(C):
            if miro[r][c] == 'J':
                J = (r, c)
                miro[r][c] = 1
            elif miro[r][c] =='F':
                q.append((r, c, 'F'))

    q.append((J[0], J[1], 'J'))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        r, c, p = q.popleft()

        if (r == 0 or r == R-1 or c == 0 or c == C-1) and p == 'J':
            print(miro[r][c])
            exit(0)

        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]
            if 0 <= x < R and 0 <= y < C and miro[x][y] == '.':
                if p == 'J':
                    miro[x][y] = miro[r][c] + 1
                else:
                    miro[x][y] = 'F'
                q.append((x, y, p))

    print('IMPOSSIBLE')