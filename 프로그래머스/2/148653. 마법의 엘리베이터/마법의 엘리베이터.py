def solution(storey):
    answer = 0
    while storey != 0:
        s, r = storey//10, storey%10
        if r > 5 or (r ==5 and s%10 >= 5):
            answer += 10-r
            s += 1
        else:
            answer += r
        storey = s

    return answer