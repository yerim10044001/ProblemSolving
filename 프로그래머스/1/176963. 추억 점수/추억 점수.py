def solution(name, yearning, photo):
    memory_score = {
        name[i]:yearning[i] for i in range(len(name))
    }
    answer = []
        
    for p in photo:
        score = 0
        for j in p:
            if j in memory_score:
                score += memory_score[j]
        answer.append(score)
        
    return answer