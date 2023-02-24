import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    
    numList = list(map(int, input().split()))
    
    dp = [numList[0]]
    maxSum = dp[0]
    for i in range(1, n):
        dp.append(max(dp[i-1]+numList[i], numList[i]))
        maxSum = max(dp[i], maxSum)
    
    print(maxSum)