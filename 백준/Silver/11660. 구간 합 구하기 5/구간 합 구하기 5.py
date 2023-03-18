import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    # make graph
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        for j in range(n):
            if i >= 1:
                graph[i][j] += graph[i-1][j]
            if j >= 1:
                graph[i][j] += graph[i][j-1]
            if i >= 1 and j >= 1:
                graph[i][j] -= graph[i-1][j-1]

    # get sum
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        x1 -= 1
        x2 -= 1
        y1 -= 1 
        y2 -= 1
        if x1 >= 1 and y1 >= 1:
            print(graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1])
        elif x1 >= 1 and y1 < 1:
            print(graph[x2][y2] - graph[x1-1][y2])
        elif x1 < 1 and y1 >= 1:
            print(graph[x2][y2] - graph[x2][y1-1])
        else:
            print(graph[x2][y2])