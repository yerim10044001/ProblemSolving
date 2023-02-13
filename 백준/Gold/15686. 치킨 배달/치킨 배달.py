import sys
input = sys.stdin.readline

def selectChicken(index, chickenCnt, distanceList):

    if index<len(chickenList) and chickenCnt < m:
        # 선택
        selectChicken(index+1, chickenCnt+1, updateMinDistance(chickenList[index], distanceList.copy()))
        # 선택 x
        selectChicken(index+1, chickenCnt, distanceList.copy())
    elif chickenCnt == m:
        global minDistance
        minDistance = min(sum(distanceList.values()), minDistance)


def updateMinDistance(chicken, distanceList):
    for house, distance in distanceList.items():
        distanceList[house] = min(distance, abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))

    return distanceList

if __name__ == "__main__":
    n, m = map(int, input().split())

    houseList = []
    chickenList = []
    for i in range(n):
        city = list(map(int, input().split()))

        # get house
        for j in range(n):
            if city[j] == 1:
                houseList.append((i, j))
            elif city[j] == 2:
                chickenList.append((i, j))

    minDistance = float("inf")

    distanceList = {}
    for house in houseList:
        distanceList[house] = float("inf")

    selectChicken(0, 0, distanceList)
    print(minDistance)