import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [0,0,1,1]
    for i in range(4, n+1):
        opCnt = dp[i-1]

        if i%3 == 0:
            opCnt = min(opCnt, dp[i//3])
        if i%2 == 0:
            opCnt = min(opCnt, dp[i//2])

        dp.append(opCnt+1)

    print(dp[n])
