import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    stair = [0]
    for _ in range(n):
        stair.append(int(input()))

    dp = [0]
    if n >= 1:
        dp.append(stair[1])
    if n >= 2:
        dp.append(stair[1]+stair[2])
    for i in range(3, n+1):
        dp.append(max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i]))

    print(dp[n])