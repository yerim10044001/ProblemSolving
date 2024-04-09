import heapq

def solution(n, k, enemy):
    heap = []
    
    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])
        if n < enemy[i]:
            while n < enemy[i] and k > 0:
                n -= heapq.heappop(heap)
                k -= 1
        if n >= enemy[i]:
            n -= enemy[i]
        else:
            return i
    return len(enemy)