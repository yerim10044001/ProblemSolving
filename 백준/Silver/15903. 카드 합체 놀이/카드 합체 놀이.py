import sys, heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))

    heapq.heapify(cards)

    for _ in range(m):
        x = heapq.heappop(cards)
        y = heapq.heappop(cards)
        heapq.heappush(cards, x+y)
        heapq.heappush(cards, x+y)
    
    print(sum(cards))