import sys
input = sys.stdin.readline
from collections import deque

def BFS(startNode):
    que = deque()
    que.append(startNode)
    visited[startNode[0]][startNode[1]] = True
    o, v = 0, 0     # 양, 늑대

    while que:
        node = que.popleft()
        if field[node[0]][node[1]] == 'o':    # 양
            o += 1
        elif field[node[0]][node[1]] == 'v':  # 늑대
            v += 1

        for w in graph[node]:
            if not visited[w[0]][w[1]]:
                visited[w[0]][w[1]] = True
                que.append(w)

    if o > v:
        return o, 0
    else:
        return 0, v

if __name__ == "__main__":
    r, c = map(int, input().split())

    field = []
    for _ in range(r):
        field.append(list(input().rstrip()))

    # make graph
    graph = {}
    for i in range(0, r):
        for j in range(0, c):
            graph[(i, j)] = []
            if i != 0 and field[i][j] != '#' and field[i-1][j] != '#':
                graph[(i-1, j)].append((i, j))
                graph[(i, j)].append((i-1, j))
            if j != 0 and field[i][j] != '#' and field[i][j-1] != '#':
                graph[(i, j-1)].append((i, j))
                graph[(i, j)].append((i, j-1))
    
    # BFS
    visited = [[False for _ in range(c)] for _ in range(r)]

    Oanswer, Vanswer = 0, 0

    for i in range(0, r):
        for j in range(0, c):
            if not visited[i][j] and field[i][j] != '#':
                o, v = BFS((i, j))
                Oanswer += o
                Vanswer += v
    
    print(Oanswer, Vanswer)
