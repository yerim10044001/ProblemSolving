import sys
input = sys.stdin.readline

def DFS(startNode):
    global depthSum
    stack = [[startNode, 0]]
    visited[startNode] = True
    
    while stack:
        node = stack.pop()
        if len(tree[node[0]]) == 1:    # if node is leaf node
            depthSum += node[1]

        for v in tree[node[0]]:
            if not visited[v]:
                visited[v] = True
                stack.append([v, node[1]+1])

if __name__ == "__main__":
    n = int(input())

    # make tree
    tree = {}
    for i in range(1, n+1):
        tree[i] = []
    
    for _ in range(n-1):
        v1, v2 = map(int, input().split())
        tree[v1].append(v2)
        tree[v2].append(v1)

    '''
    if sum of leaf node's depth is odd, win and even, lose
    '''
    visited = [False for _ in range(0, n+1)]
    depthSum = 0
    DFS(1)
    if depthSum%2 == 0:
        print("No")
    else:
        print("Yes")