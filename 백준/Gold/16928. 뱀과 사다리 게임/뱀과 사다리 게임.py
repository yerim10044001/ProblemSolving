import sys
input = sys.stdin.readline
from collections import deque


if __name__ == "__main__":
    n, m = map(int, input().split())

    gamepan = [0] * 101
    for _ in range(n+m):
        x, y = map(int, input().split())
        gamepan[x] = y

    q = deque([1])
    gameCnt = [0] * 101
    gameCnt[1] = 1
    while q:
        curr = q.popleft()
        if curr == 100: break

        for i in range(1, 7):
            if curr+i <= 100:
                if gameCnt[curr+i] == 0 and gamepan[curr+i] != 0:   # 사다리 or 뱀 있는가?
                    if gameCnt[gamepan[curr+i]] == 0:   
                        gameCnt[gamepan[curr+i]] = gameCnt[curr]+1
                        q.append(gamepan[curr+i])
                    gameCnt[curr+i] = gameCnt[curr]+1

                elif gameCnt[curr+i] == 0: # 사다리 or 뱀 없음
                    gameCnt[curr+i] = gameCnt[curr]+1
                    q.append(curr+i)

    
    print(gameCnt[curr]-1)