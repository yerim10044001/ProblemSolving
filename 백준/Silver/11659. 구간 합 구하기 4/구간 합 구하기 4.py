import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    dp = [0]
    numList = list(map(int, input().split()))

    sum = 0
    for i in numList:
        sum += i
        dp.append(sum)

    for i in range(m):
        i, j = map(int, input().split())
        print(dp[j]-dp[i-1])