import sys
input = sys.stdin.readline

def getSum(numList):
    answer, i = 0, 0
    while True:
        if i+1 < len(numList):
            answer += max(numList[i]*numList[i+1], numList[i]+numList[i+1])
        elif i < len(numList):
            answer += numList[i]
        else:
            break
        i += 2
    return answer

if __name__ == "__main__":
    # get input
    n = int(input())
    positiveList = []
    negativeList = []
    hasZero = False
    for _ in range(n):
        num = int(input())
        if num > 0: positiveList.append(num)
        elif num < 0: negativeList.append(num)
        else:
            hasZero = True

    # sort
    positiveList.sort(reverse=True)
    negativeList.sort()
    if hasZero:
        negativeList.append(0)

    # get sum
    answer = 0
    answer += getSum(positiveList)
    answer += getSum(negativeList)

    print(answer)
    