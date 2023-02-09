import sys
input = sys.stdin.readline

def canDrink(s):
    drinkSum = 0
    for i in range(0,n):
        if s > Rlist[i]:     # 주량 한계보다 s가 클 때,
            drinkSum += Rlist[i]
        else:
            drinkSum += s
    
    if drinkSum >= t: # 다른 사람이 더 마실 수 있음
        return True
    else:
        return False

if __name__ == "__main__":
    n, t = map(int, input().split())

    Llist = []
    Rlist = []

    for _ in range(0, n):
        Li, Ri = map(int, input().split()) 
        Llist.append(Li)
        Rlist.append(Ri)

    # S에 관계없이 항상 불가능
    LSum, RSum = sum(Llist), sum(Rlist)
    if LSum > t or RSum < t:
        print(-1)
        exit(0)
    
    # 이분탐색 시작
    left, right = max(Llist),max(Rlist)

    answer = right + 1
    while left <= right:
        s = (left+right)//2

        if canDrink(s):
            answer = min(answer, s)
            right = s-1
        else:
            left = s+1

    print(answer)