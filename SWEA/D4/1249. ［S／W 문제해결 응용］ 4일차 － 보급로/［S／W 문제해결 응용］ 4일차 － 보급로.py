from collections import deque
def solve(maps, n):
    def bfs():
        visited = [[100000] * n for _ in range(n)]
        visited[0][0] = 0
        q = deque()
        q.append((0, 0, 0))

        while q:
            x, y, w = q.popleft()
            for dx, dy in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
                if 0 <= x+dx < n and 0 <= y+dy < n:
                    if visited[x+dx][y+dy]>maps[x+dx][y+dy]+w:
                        visited[x+dx][y+dy] = maps[x+dx][y+dy]+w
                        q.append((x+dx, y+dy, maps[x+dx][y+dy]+w))
        return visited[n-1][n-1]

    return bfs()


if __name__ == '__main__':
    t = int(input())
    for c in range(1, t + 1):
        n = int(input())
        maps = [list(map(int, list(input()))) for _ in range(n)]
        answer = solve(maps, n)
        print(f'#{c} {answer}')
