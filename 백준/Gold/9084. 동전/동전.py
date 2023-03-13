import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        coins = list(map(int, input().split()))
        cost = int(input())

        dp = [0] * (cost+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, cost+1):
                dp[i] += dp[i-coin]
        
        print(dp[cost])

