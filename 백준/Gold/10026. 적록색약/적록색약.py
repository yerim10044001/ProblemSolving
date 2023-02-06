import sys
input = sys.stdin.readline

def DFS(i, j):
    stack = [(i, j)]
    while stack:
        node = stack.pop()
        visited[node[0]][node[1]] = True
        for v in normalGraph[node]:
            if not visited[v[0]][v[1]]:
                stack.append(v)

def DFS_c(i, j):
    stack = [(i, j)]
    while stack:
        node = stack.pop()
        colorBlindVisited[node[0]][node[1]] = True
        for v in colorBlindGraph[node]:
            if not colorBlindVisited[v[0]][v[1]]:
                stack.append(v)

if __name__ == "__main__":
    n = int(input())

    picture = []
    for _ in range(0, n):
        picture.append(list(input().rstrip()))

    # make graph
    normalGraph = {}
    colorBlindGraph = {}

    for i in range(0, n):
        for j in range(0, n):
            normalGraph[(i, j)] = []
            colorBlindGraph[(i, j)] = []
            if i != 0:  # top line
                if picture[i][j] == picture[i-1][j]:
                    normalGraph[(i, j)].append((i-1, j))
                    normalGraph[(i-1, j)].append((i, j))
                    colorBlindGraph[(i, j)].append((i-1, j))
                    colorBlindGraph[(i-1, j)].append((i, j))
                elif (picture[i][j] == 'R' and picture[i-1][j] == 'G') or (picture[i][j] == 'G' and picture[i-1][j] == 'R'):
                    colorBlindGraph[(i, j)].append((i-1, j))
                    colorBlindGraph[(i-1, j)].append((i, j))
                
            if j != 0:  # left line
                if picture[i][j] == picture[i][j-1]:
                    normalGraph[(i, j)].append((i, j-1))
                    normalGraph[(i, j-1)].append((i, j))
                    colorBlindGraph[(i, j)].append((i, j-1))
                    colorBlindGraph[(i, j-1)].append((i, j))
                elif (picture[i][j] == 'R' and picture[i][j-1] == 'G') or (picture[i][j] == 'G' and picture[i][j-1] == 'R'):
                    colorBlindGraph[(i, j)].append((i, j-1))
                    colorBlindGraph[(i, j-1)].append((i, j))

    # DFS
    visited = [[False for _ in range(0,n)] for _ in range(0,n)]
    colorBlindVisited = [[False for _ in range(0,n)] for _ in range(0,n)]
    normalCount = 0
    colorBlindCount = 0
    for i in range(0, n):
        for j in range(0, n):
            if not visited[i][j]:
                DFS(i, j)
                normalCount += 1
            if not colorBlindVisited[i][j]:
                DFS_c(i, j)
                colorBlindCount += 1

    print(normalCount, colorBlindCount)

