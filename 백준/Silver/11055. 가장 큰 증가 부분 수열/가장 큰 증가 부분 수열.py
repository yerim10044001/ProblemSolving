import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    numList = list(map(int, input().split()))

    dp = [numList[0]]
    for i in range(1, n):
        dp.append(numList[i])
        for j in range(0,i):
            if numList[j] < numList[i]:
                dp[i] = max(dp[j]+numList[i], dp[i])
    
    print(max(dp))