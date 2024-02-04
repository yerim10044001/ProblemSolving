import math

def solution(r1, r2):
    answer = 0
    # 제 1사분면
    for x in range(1, r2+1):
        y_max = math.floor(math.sqrt(math.pow(r2,2) - math.pow(x,2)))
        y_min = 0
        if r1 > x:
            y_min = math.ceil(math.sqrt(math.pow(r1,2) - math.pow(x,2)))
            
        answer += y_max - y_min + 1
        
    return answer*4