import sys
input = sys.stdin.readline
import heapq

if __name__ == "__main__":
    n = int(input())
    classList = [ list(map(int, input().split())) for _ in range(n) ]

    classList.sort(key=lambda p: (p[0],p[1]))
    heapQue = []
    heapq.heappush(heapQue, classList.pop(0)[1])

    for i in range(n-1):
        prevEnd = heapq.heappop(heapQue)
        if classList[i][0] < prevEnd:
            heapq.heappush(heapQue, prevEnd)
        heapq.heappush(heapQue,classList[i][1])

    
    print(len(heapQue))