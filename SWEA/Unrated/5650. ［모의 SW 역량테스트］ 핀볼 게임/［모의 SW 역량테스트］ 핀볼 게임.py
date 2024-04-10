
'''
return next_direction
'''
def change_direction(block_num, direction):
    if block_num == 1:
        if direction == 1: return 2
        elif direction == -2:  return -1
        else: return direction * (-1)
    elif block_num == 2:
        if direction == -2: return 1
        elif direction == -1:  return 2
        else: return direction * (-1)
    elif block_num == 3:
        if direction == -1: return -2
        elif direction == 2:  return 1
        else: return direction * (-1)
    elif block_num == 4:
        if direction == 1: return -2
        elif direction == 2:  return -1
        else: return direction * (-1)
    elif block_num == 5:
        return direction * (-1)

'''
direction
-1 : up
1 : down
-2 : left
2 : right
'''
def game(startX, startY, direction, n, gamepan, wormholes):
    score = 0
    x, y = startX, startY
    while True:
        # 방향따라 위치이동
        if direction == -1: x -= 1
        elif direction == 1: x += 1
        elif direction == -2: y -= 1
        elif direction == 2: y += 1

        if x == -1 or x == n or y == -1 or y == n: # 벽에 부딪힘
            direction = change_direction(5, direction)
            score += 1
        elif 0 <= x <= n-1 and 0 <= y <= n-1:
            block_num = gamepan[x][y]
            # 블록
            if 1 <= block_num <= 5:
                direction = change_direction(block_num, direction)
                score += 1
            # 웜홀
            elif 6 <= block_num <= 10:
                next_x_y = list(filter(lambda p: p != [x, y], wormholes[block_num]))
                x, y = next_x_y[0][0], next_x_y[0][1]
            # 블랙홀 또는 시작위치 game over
            elif gamepan[x][y] == -1 or (x == startX and y == startY):
                break

    return score



if __name__ == "__main__":
    t = int(input())

    for test_i in range(1, t+1):
        answer = 0
        # input
        n = int(input())
        gamepan = []
        wormholes = { 6: [], 7: [], 8: [], 9: [], 10: [] }
        for i in range(n):
            gamepan.append(list(map(int, input().split())))
            # get wormhole location
            for j in range(n):
                if 6 <= gamepan[i][j] <= 10:
                    wormholes[gamepan[i][j]].append([i, j])

        # game start
        for i in range(n):
            for j in range(n):
                if gamepan[i][j] == 0:
                    answer = max(answer,
                                 game(i, j, -1, n, gamepan, wormholes),
                                 game(i, j, 1, n, gamepan, wormholes),
                                 game(i, j, -2, n, gamepan, wormholes),
                                 game(i, j, 2, n, gamepan, wormholes))
        print(f"#{test_i} {answer}")
