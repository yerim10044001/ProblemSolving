import sys
input = sys.stdin.readline
from collections import deque

MAX = 100001

if __name__ == "__main__":
    n, k = map(int, input().split())

    time = [0] * MAX
    prevLocation = [0] * MAX

    time[n] = 1
    q = deque([n])

    while q:
        curr = q.popleft()
        if curr == k: 
            print(time[k]-1)
            break

        for x in [curr-1, curr+1, 2*curr]:
            if 0 <= x < MAX and time[x] == 0:
                time[x] = time[curr]+1
                prevLocation[x] = curr
                q.append(x)
        
    
    result = []
    while n != k:
        result.append(k)
        k = prevLocation[k]
    result.append(k)
    result.reverse()
    print(' '.join(list(map(str, result))))
