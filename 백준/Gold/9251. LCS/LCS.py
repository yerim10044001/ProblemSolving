import sys
input = sys.stdin.readline

if __name__ == "__main__":
    str1 = input().rstrip()
    str2 = input().rstrip()

    dp = [0] * len(str2)

    for i in range(len(str1)):
        prevMaxLength = 0
        for j in range(len(str2)):
            if prevMaxLength < dp[j]:   
                prevMaxLength = dp[j]
            elif str1[i] == str2[j]:    # 문자가 같은 경우
                dp[j] = prevMaxLength+1

    print(max(dp))