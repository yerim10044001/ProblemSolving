import sys, heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    classList = [ list(map(int, input().split())) for _ in range(n) ]
    classList.sort()

    heapQue = [0]

    for start, end in classList:
        prevEnd = heapq.heappop(heapQue)
        if start < prevEnd:
            heapq.heappush(heapQue, prevEnd)
        heapq.heappush(heapQue,end)

    print(len(heapQue))