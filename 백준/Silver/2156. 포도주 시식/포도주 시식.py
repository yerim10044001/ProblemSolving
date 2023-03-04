import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    grape = []
    for _ in range(n):
        grape.append(int(input()))

    dp = [grape[0]]
    if n == 1:
        print(grape[0])
        exit(0)
    if n == 2:
        print(grape[0]+grape[1])
        exit(0)

    dp.append(grape[0]+grape[1])
    dp.append(max(grape[0]+grape[1], grape[0]+grape[2], grape[1]+grape[2]))
    for i in range(3, n):
        dp.append(max(dp[i-3]+grape[i-1]+grape[i], dp[i-2]+grape[i], dp[i-1]))
    print(dp[n-1])
