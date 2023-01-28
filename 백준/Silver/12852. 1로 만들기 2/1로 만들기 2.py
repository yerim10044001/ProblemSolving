import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    dp = [0 for _ in range(0, n+1)]
    prevList = [0 for _ in range(0, n+1)]

    for i in range(2, n+1):
        dp[i] = dp[i-1]+1
        prevList[i] = i-1
        if i % 3 == 0 and dp[i//3]+1 < dp[i]:
            dp[i] = dp[i//3]+1
            prevList[i] = i//3
        if i % 2 == 0 and dp[i//2]+1 < dp[i]:
            dp[i] = dp[i//2]+1
            prevList[i] = i//2

    print(dp[n])

    # get numList
    while prevList[n] != 0:
        print(n, end = ' ')
        n = prevList[n]
    print(n, end = ' ')