import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    cost = list(map(int, input().split()))

    dp = []
    for i in range(0, n):
        dp.append(cost[i])

        for j in range(i-1, i//2-1, -1):
            dp[i] = max(dp[i], dp[j]+dp[i-j-1])
    
    print(dp[n-1])
