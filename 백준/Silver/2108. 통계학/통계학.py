import sys
input = sys.stdin.readline
def getMaxCont(numCount):
    maxKey = []
    maxCount = 0
    for key, value in numCount.items():
        if value > maxCount:
            maxKey = [key]
            maxCount = value
        elif value == maxCount:
            maxKey.append(key)
    
    if len(maxKey) >= 2:
        maxKey.sort()
        return maxKey[1]
    else:
        return maxKey[0]

if __name__ == "__main__":
    n = int(input())
    numList = []
    numCount = {}

    for _ in range(0, n):
        num = int(input())
        numList.append(num)

        # for count
        if num in numCount:
            numCount[num] += 1
        else:
            numCount[num] = 1

    numList.sort()

    # 산술평균  
    print(round(sum(numList)/n))
    # 중앙값
    print(numList[n//2])
    # 최빈값
    print(getMaxCont(numCount))
    # 범위
    print(numList[-1] - numList[0])

