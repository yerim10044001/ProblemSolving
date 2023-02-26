import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    numList = list(map(int, input().split()))

    dp = [1]
    for i in range(1, n):
        dp.append(1)
        for j in range(0, i):
            if numList[j] < numList[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    print(max(dp))