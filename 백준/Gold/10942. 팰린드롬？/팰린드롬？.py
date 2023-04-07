import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    # make dp
    dp = [[0]*(n+1) for _ in range (n+1)]
    for i in range(n, 0, -1):
        for j in range(i, n+1):
            if j-i > 1:
                if dp[i+1][j-1] == 1 and numbers[i-1] == numbers[j-1]:
                    dp[i][j] = 1
            elif numbers[i-1] == numbers[j-1]:
                dp[i][j] = 1


    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        print(dp[s][e])