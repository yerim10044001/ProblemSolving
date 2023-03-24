import sys
from datetime import datetime, timedelta
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    flowers = []
    for _ in range(n):
        startMonth, startDay, endMonth, endDay = map(int, input().split())

        # princess season border check
        if startMonth < 3: startMonth, startDay = 3, 1
        if endMonth > 11: endMonth, endDay = 12, 1
        
        start = startMonth*100 + startDay
        end = endMonth*100 + endDay
        if end-start > 0: flowers.append((start, end))
    
    # sort by starting date
    flowers.sort(key= lambda p: (p[0], -p[1]))

    # initial flower
    selectedFlower = flowers.pop(0)
    start = selectedFlower[0]
    end = selectedFlower[1]

    # select flowers
    answer = 1
    while start == 301:
        if len(flowers) == 0 or end == 1201: break

        for flower in flowers[:]:
            if flower[0] <= end and flower[1] > selectedFlower[1]:
                selectedFlower = flower
                flowers.remove(flower)
            elif flower[0] <= end:
                flowers.remove(flower)
            else: break
        
        # if blank between flowers break
        if end == selectedFlower[1]: break

        end = selectedFlower[1]
        answer += 1

    # print answer
    if start == 301 and end == 1201: print(answer)
    else: print(0)