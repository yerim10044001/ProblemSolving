import sys
input = sys.stdin.readline


if __name__ == "__main__":
    dp = [0, 1, 2, 4]

    t = int(input())

    for _ in range(t):
        n = int(input())
        if len(dp) <= n:
            for i in range(len(dp), n+1):
                dp.append((dp[i-1]+dp[i-2]+dp[i-3])%1000000009)

        print(dp[n]%1000000009)