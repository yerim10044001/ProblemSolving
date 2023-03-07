import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    dp = [1]*10
    i = 1
    while i < n:
        for j in range(1, 10):
            dp[j] += dp[j-1]
        i += 1

    print(sum(dp)%10007)

