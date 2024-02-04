from collections import deque

def solution(targets):
    # e 기준 오름차순 정렬
    targets.sort(key=lambda x: x[1])
    
    # 최소 요격 미사일 수 계산
    answer = 1
    x = targets[0][1] - 0.5
    
    q = deque(targets)
    while q:
        roket = q.popleft()
        if roket[0]+0.5 > x:
            x = roket[1]-0.5
            answer += 1
        
    return answer