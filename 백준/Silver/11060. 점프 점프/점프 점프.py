import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    n = int(input())
    miro = list(map(int, input().split()))
    
    dp = [n+1]*n
    dp[0] = 0
    
    q = deque([0])
    while q:
        p = q.popleft()

        for i in range(1, miro[p]+1):
            if p+i < n and dp[p+i] > dp[p] + 1:
                q.append(p+i)
                dp[p+i] = dp[p] + 1
            
    if dp[n-1] != n+1:
        print(dp[n-1])
    else:
        print(-1)