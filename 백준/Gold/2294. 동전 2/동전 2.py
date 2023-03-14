import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())

    coins = []
    for _ in range(n):
        coins.append(int(input()))
    dp = [0]

    for i in range(1, k+1):
        dp.append(k+1)
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)

    if dp[k] == k+1:
        print(-1)
    else:
        print(dp[k])