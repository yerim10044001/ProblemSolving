import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    numList = list(map(int, input().split()))

    dp = [1]
    prev = [0]
    maxIndex = 0
    for i in range(1, n):
        dp.append(1)
        prev.append(i)
        for j in range(0, i):
            if numList[j] < numList[i] and dp[i]<dp[j]+1:
                dp[i] = dp[j]+1
                prev[i] = j
        
        # find max sequence
        if dp[i] > dp[maxIndex]:
            maxIndex = i

    # get sequence number
    i = maxIndex
    result = []
    while prev[i] != i:
        result.append(numList[i])
        i = prev[i]
    result.append(numList[i])

    result.reverse()
    result = list(map(str, result))
    print(dp[maxIndex])
    print(" ".join(result))