import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    miro = list(map(int, input().split()))
    
    dp = [n+1]*n
    dp[0] = 0
    
    for p in range(0, n):
        for i in range(1, miro[p]+1):
            if p+i < n and dp[p+i] > dp[p] + 1:
                dp[p+i] = dp[p] + 1
            
    if dp[n-1] != n+1:
        print(dp[n-1])
    else:
        print(-1)