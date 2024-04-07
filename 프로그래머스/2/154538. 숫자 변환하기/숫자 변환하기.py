from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque()
    visited = set()
    
    queue.append([x, 0])
    visited.add(x)

    while queue:
        k, cnt = queue.popleft()
        
        if k+n == y or k*2 == y or k*3 == y:
            return cnt+1
        if k+n < y and k+n not in visited:
            queue.append([k+n, cnt+1])
            visited.add(k+n)
        if k*2 < y and k*2 not in visited:
            queue.append([k*2, cnt+1])
            visited.add(k*2)
        if k*3 < y and k*3 not in visited:
            queue.append([k*3, cnt+1])
            visited.add(k*3)
        
    return -1