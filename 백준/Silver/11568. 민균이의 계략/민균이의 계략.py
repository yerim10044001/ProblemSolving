if __name__ == "__main__":
    n = int(input())
    numList = list(map(int,input().split()))

    cntList = [0 for _ in range (0, n)]
    maxCnt = 0
    for i in range(0, n):
        cnt = 1
        for j in range(0, i):
            if numList[j] < numList[i] and cnt < (cntList[j]+1):
                cnt = cntList[j] + 1

        # update maxCnt
        if maxCnt < cnt:
            maxCnt = cnt
        cntList[i] = cnt

    print(maxCnt)