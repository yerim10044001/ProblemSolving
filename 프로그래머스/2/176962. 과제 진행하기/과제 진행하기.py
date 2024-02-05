from collections import deque

def solution(plans):
    def time_calc(t):
        if type(t) == type(1):
            return t
        hh, mm = map(int, t.split(":"))
        return hh*60 + mm
    
    answer = []
    
    # plans 시간 순으로 정렬
    plans.sort(key=lambda x: x[1])

    # 첫 번째 과제
    stack = deque()
    first_plan = plans[0]
    stack.append(first_plan)

    # plans에 있는 과제 시작하기
    for plan in plans[1:]:
        current_time = plan[1]
        # 시간이 남았을 때 멈춰둔 과제 하기
        while stack:
            # 현재시간 - 이전 과제 시작시간 >= 이전과제 playtime
            if time_calc(current_time) - time_calc(stack[-1][1]) >= int(stack[-1][2]):
                complete_plan = stack.pop()
                answer.append(complete_plan[0])
                # 남아있는 과제의 시작시간 초기화
                if stack:
                    stack[-1][1] = time_calc(complete_plan[1])+int(complete_plan[2])
            # 멈춰 둔 과제를 끝내지 못할 경우 남은 시간, 시작시간 초기화
            else:
                stack[-1][2] = int(stack[-1][2]) - (time_calc(current_time) - time_calc(stack[-1][1]))
                stack[-1][1] = current_time
                break
                
        stack.append([plan[0], current_time, plan[2]])
    
    
    # 새로 시작해야 하는 과제가 더 이상 없을 때, 멈춰둔 과제 하기
    while stack:
        plan = stack.pop()
        answer.append(plan[0])
    
    return answer
