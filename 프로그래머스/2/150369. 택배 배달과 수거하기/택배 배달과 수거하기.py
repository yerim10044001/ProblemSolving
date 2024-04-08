def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:
        max_distance = 0
        
        # ->
        curr_cap = cap
        while deliveries and curr_cap > 0:
            if deliveries[-1] == 0:          # 배달 없음
                deliveries.pop()
            elif deliveries[-1] <= curr_cap: # 배달 가능
                max_distance = max(max_distance, len(deliveries))
                curr_cap -= deliveries.pop()
            else:                            # 일부 배달 가능
                deliveries[-1] -= curr_cap
                max_distance = max(max_distance, len(deliveries))
                break 
        # <-
        curr_cap = cap
        while pickups and curr_cap > 0:
            if pickups[-1] == 0:          # 수거 없음
                pickups.pop()
            elif pickups[-1] <= curr_cap: # 수거 가능
                max_distance = max(max_distance, len(pickups))
                curr_cap -= pickups.pop()
            else:                            # 일부 수거 가능
                pickups[-1] -= curr_cap
                max_distance = max(max_distance, len(pickups))
                break 
        
        # 이동 거리
        answer += max_distance
        
    return answer*2