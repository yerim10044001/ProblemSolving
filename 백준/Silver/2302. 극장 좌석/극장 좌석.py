import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    fixList = []
    for _ in range(m):
        fixList.append(int(input()))

    fixList.append(n+1)

    answer = 1
    start = 1
    dp = [1, 1, 2]
    for i in fixList:
        for j in range(3, i-start+1):
            if len(dp) <= j:
                dp.append(dp[j-1]+dp[j-2])

        answer *= dp[i-start]
        start = i+1
    
    print(answer)