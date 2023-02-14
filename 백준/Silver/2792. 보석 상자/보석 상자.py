import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    jewelList = []
    for _ in range(m):
        jewelList.append(int(input()))

    answer = max(jewelList)
    left, right = 1, answer
    
    while left <= right:
        mid = (left+right)//2

        peopleCnt = 0       # 최대 mid만큼 보석을 주었을 때 보석을 나누어줄 수 있는 사람 수
        for jewel in jewelList:
            peopleCnt += jewel//mid

            if jewel%mid != 0:
                peopleCnt += 1
        
        # 사람들에게 보석을 더 줘야하는 경우
        if peopleCnt > n:
            left = mid+1
        else:
            answer = min(answer, mid)
            right = mid-1
    
    print(answer)
