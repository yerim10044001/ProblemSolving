def solution(picks, minerals):
    # 가진 곡괭이 수
    pick_num = sum(picks)
    
    # 광물 5개씩 자르기
    mineral_priority = []
    for i in range(0, pick_num):
        # 마지막 남은 광물이 5개 아닐 때,
        unit = 5

        if (i+1)*5 > len(minerals):
            unit = len(minerals) - i*5

        priority = 0
        for mineral in minerals[i*5:i*5+unit]:
            if mineral == "diamond":
                priority += 25
            elif mineral == "iron":
                priority += 5
            else:
                priority += 1
        mineral_priority.append([priority, minerals[i*5:i*5+unit]])
        
        # 곡괭이 수*5 가 광물 수 보다 더 많을 때, 광물 추가 stop
        if unit != 5:
            break
    
    # 피로도 계산
    answer = 0
    mineral_priority.sort(key=lambda x: x[0]) # 우선순위 낮은 순으로 정렬
    
    # 다이아몬드 곡괭이 사용
    for i in range(0, picks[0]):
        if mineral_priority:
            p, m_list = mineral_priority.pop()
            
            for m in m_list:
                answer += 1
            
    # 철 곡괭이 사용
    for i in range(0, picks[1]):
        if mineral_priority:
            p, m_list = mineral_priority.pop()
            
            for m in m_list:
                if m == "diamond":
                    answer += 5
                else:
                    answer += 1
    # 돌 곡괭이 사용
    for i in range(0, picks[2]):
        if mineral_priority:
            p, m_list = mineral_priority.pop()
            
            for m in m_list:
                if m == "diamond":
                    answer += 25
                elif m == "iron":
                    answer += 5
                else:
                    answer += 1
        
    return answer