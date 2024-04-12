import sys
input = sys.stdin.readline

def dummy(n, apples, snake_direction):
    snake = []
    snake.append((1, 1))

    # set border
    visited = [ [False]*(n+2) for _ in range (n+2) ]
    visited[0] = [True]*(n+2) 
    visited[n+1] = [True]*(n+2) 
    for i in range(1, n+1):
        visited[i][0] = True
        visited[i][n+1] = True
    visited[1][1] = True

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]


    time, d = 0, 0
    if snake_direction:
        change_direction = snake_direction.pop(0)
    else:
        change_direction = [-1, 0]
    while True:
        # change direction
        if time == int(change_direction[0]):
            if change_direction[1] == 'D': d = (d+1)%4
            elif change_direction[1] == 'L': d = (d-1)%4
            if snake_direction:
                change_direction = snake_direction.pop(0)

        # move
        nextX, nextY = snake[0][0]+dx[d], snake[0][1]+dy[d]
        # game over
        if visited[nextX][nextY]: break

        # eat apple
        if (nextX, nextY) not in apples:
            tailX, tailY = snake.pop()
            visited[tailX][tailY] = False
        else:
            apples.remove((nextX, nextY))
        
        snake.insert(0, (nextX, nextY))
        visited[nextX][nextY] = True
        time += 1

    return time+1

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    apples = set()
    for _ in range(k):
        x, y = map(int, input().split())
        apples.add((x, y))
    l = int(input())
    snake_direction = []
    for _ in range(l):
        snake_direction.append(input().split())

    print(dummy(n, apples, snake_direction))