def solution(sequence, k):
    
    answer = []
    right = 0
    sequence_sum = 0
    for left in range(len(sequence)):
        
        while right<len(sequence) and sequence_sum < k:
            sequence_sum += sequence[right]
            right += 1
            
        if sequence_sum == k:
            answer.append([left, right-1, right-left+1])
        sequence_sum -= sequence[left]
            
    answer.sort(key= lambda x: x[2])
    return [answer[0][0], answer[0][1]]

        