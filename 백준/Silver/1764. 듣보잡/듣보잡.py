import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    nameDic = {}
    resultList = []
    for i in range(0, n):
        name = input().rstrip()
        nameDic[name] = True
    
    for j in range(0, m):
        name = input().rstrip()
        if name in nameDic:
            resultList.append(name)
    
    # print result
    resultList.sort()
    print(len(resultList))
    for i in resultList:
        print(i)
