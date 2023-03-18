import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    # make graph
    graph = [[0] * (n+1)]
    for i in range(1, n+1):
        graph.append([0] + list(map(int, input().split())))
        for j in range(1, n+1):
            graph[i][j] += graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1]

    # get sum
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1])