import sys
input = sys.stdin.readline
import math

def getMinSqrtCnt(n):
    if  n**(0.5)%1 == 0:
        return 1
    
    minSqrtCnt = n
    for i in range(1, int(math.trunc(math.sqrt(n)))+1):
        minSqrtCnt = min(minSqrtCnt, dp[n - i**2]+1)
    
    return minSqrtCnt


if __name__ == "__main__":
    n = int(input())

    if  n**(0.5)%1 == 0:
            print(1)
            exit(0)

    dp = [0, 1, 2]
    for i in range(3, n+1):
        dp.append(getMinSqrtCnt(i))

    print(dp[n])


