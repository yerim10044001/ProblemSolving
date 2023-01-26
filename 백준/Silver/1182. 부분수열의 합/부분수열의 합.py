import sys
input = sys.stdin.readline

def subset(numList, index, s):
    if index < len(numList):
        x = numList[index]
        subset(numList, index+1, s-x) # 선택한 경우
        subset(numList, index+1, s)   # 선택안한 경우
    elif s == 0:
        global result
        result += 1


if __name__ == "__main__":
    n, s = map(int, input().split())

    numList = list(map(int, input().split()))

    result = 0
    if s == 0:      # s가 0인경우 공집합 제외
        result -= 1
    subset(numList, 0, s)
    print(result)