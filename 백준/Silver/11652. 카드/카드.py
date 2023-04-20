import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    maxNum = 0
    maxCnt = 0
    numList = {}
    for _ in range(n):
        num = int(input())
        try:
            numList[num] += 1
        except:
            numList[num] = 1
        if numList[num] == maxCnt:
                maxNum = min(num, maxNum)
        elif numList[num] > maxCnt:
            maxNum = num
            maxCnt = numList[num]
    
    print(maxNum)