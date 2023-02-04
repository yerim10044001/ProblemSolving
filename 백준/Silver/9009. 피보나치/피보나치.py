import sys
input = sys.stdin.readline

# n보다 크지 않은 가장 작은 피보나치 수 찾기
def getFibo(n, fiboList):
    k = 2

    while fiboList[k] <= n:
        k += 1
        if len(fiboList) == k: 
            fiboList.append(fiboList[k-1]+fiboList[k-2])
    return fiboList[k-1]


if __name__ == "__main__":
    testNum = int(input())

    fiboList = [0, 1, 1]
    
    for _ in range(testNum):
        n = int(input())
        minFiboList = []
        while n != 0:
            minFiboList.append(getFibo(n, fiboList))
            n -= minFiboList[-1]
            
        # print minFiboList
        minFiboList.reverse()
        print(' '.join(map(str, minFiboList)))
