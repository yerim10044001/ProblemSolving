import sys
input = sys.stdin.readline

def getSum(n):
    if len(dp) <= n:
        for i in range(len(dp), n+1):
            dp.append(dp[i-3]+i//2+1)
    
    return dp[n]

if __name__ == "__main__":
    dp = [0, 1, 2, 3, 4]

    t = int(input())

    for _ in range(t):
        print(getSum(int(input())))