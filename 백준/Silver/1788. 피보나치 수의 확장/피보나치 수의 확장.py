import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    if n < 0 and n%2 == 0:
        print(-1)
    elif n == 0:
        print(0)
    else:
        print(1)

    n = abs(n)
    dp = [0, 1, 1]
    for i in range(3, n+1):
        dp.append((dp[i-1]+dp[i-2])%1000000000)
    
    print(dp[n])