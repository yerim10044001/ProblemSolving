import sys
input = sys.stdin.readline

def dfsStack(graph, node, visited):
    stack = [node]

    while stack:
        v = stack.pop()
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                parent[w] = v
                stack.append(w)

if __name__ == "__main__":
    n = int(input())

    # initialize graph
    graph = {}
    for i in range(1,n+1):
        graph[i]= []

    # add edge
    for _ in range(0,n-1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # dfs search
    visited = [False for _ in range(0, n+1)]
    parent = [ None for _ in range(0, n+1)]
    dfsStack(graph, 1, visited)

    # get result
    for i in range(2, n+1):
        print(parent[i])