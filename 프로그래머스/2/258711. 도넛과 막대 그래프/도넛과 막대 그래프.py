from collections import deque

def solution(edges):
    
    graph = {}
    nodes = set()
    
    # make graph
    for a, b in edges:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
            nodes.add(b)
        
    # find new node 
    for i in graph:
        if (len(graph[i]) >= 2) and (i not in nodes):
            new_node = i
            break
    
    # get graph num by dfs
    visited = set()
    answer = [new_node, 0, 0, 0]

    for v in graph[new_node]:
        # dfs start
        q = deque()
        q.append(v)
        find_type = False
        while q:
            node = q.pop()
            if node not in visited: 
                # find graph type
                if node not in graph:
                    answer[2] += 1  # stick
                    find_type = True
                    break
                elif len(graph[node]) > 1: 
                    answer[3] += 1  # 8
                    find_type = True
                    break
                
                visited.add(node)
                q.extend(graph[node])
        if not find_type: # donut
            answer[1] += 1
    
    return answer