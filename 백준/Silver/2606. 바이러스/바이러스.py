import sys
input = sys.stdin.readline

def dfsSearch(vertex):
    global result
    for v in graph[vertex]:
        if not visited[v]:
            visited[v] = True
            result += 1
            dfsSearch(v)

if __name__ == "__main__":
    n = int(input())
    edgeCnt = int(input())

    # 그래프 초기화
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    for _ in range(0, edgeCnt):
        com1, com2 = map(int, input().split())
        graph[com1].append(com2)
        graph[com2].append(com1)

    # dfs search
    visited = [False for _ in range(0, n+1)]
    visited[1] = True
    result = 0
    dfsSearch(1)

    print(result)

    