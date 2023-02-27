import sys
input = sys.stdin.readline

if __name__ == "__main__":
    dp = [1, 1, 1, 2, 2]

    t = int(input())
    for _ in range(t):
        n = int(input())

        for i in range(5, n):
            if len(dp)<= i:
                dp.append(dp[i-1]+dp[i-5])
        print(dp[n-1])