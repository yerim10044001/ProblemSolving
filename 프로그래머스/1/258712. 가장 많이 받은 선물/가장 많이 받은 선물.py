def solution(friends, gifts):
    # this month gifts
    # 준 선물 수 메모
    gift_memo = [[0]*len(friends) for _ in range(len(friends))]
    
    for gift in gifts:
        A, B = gift.split()
        a_index = friends.index(A)
        b_index = friends.index(B)
        
        # gift num 선물지수
        gift_memo[a_index][a_index] += 1
        gift_memo[b_index][b_index] -= 1
        
        # A->B 
        gift_memo[a_index][b_index] += 1
    
    
    # next month gifts
    next_gift_memo = [0 for _ in range (len(friends))]
    for i in range(0, len(friends)):
        for j in range(i+1, len(friends)):
            if gift_memo[i][j] > gift_memo[j][i]:
                next_gift_memo[i] += 1
            elif gift_memo[i][j] < gift_memo[j][i]:
                next_gift_memo[j] += 1
            else:
                if gift_memo[i][i] > gift_memo[j][j]:
                    next_gift_memo[i] += 1
                elif gift_memo[i][i] < gift_memo[j][j]:
                    next_gift_memo[j] += 1
                
    answer = max(next_gift_memo)
    return answer