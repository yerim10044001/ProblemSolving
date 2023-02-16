import sys
input = sys.stdin.readline

def getSumCnt(n):
    for i in range(4, n+1):
        if len(dp) == i:
            dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    
    return dp[n]

if __name__ == "__main__":
    t = int(input())

    dp = [0,1,2,4]

    for _ in range(t):
        n = int(input())
        print(getSumCnt(n))
