def solution(players, callings):

    player_dic = {players[i]:i for i in range(len(players))}
    player_dic_rev = { i:players[i] for i in range(len(players))}
    
    for p in callings:
        rank = player_dic[p]
        player_dic[player_dic_rev[rank-1]] += 1
        
        player_dic_rev[rank] = player_dic_rev[rank-1]
        player_dic_rev[rank-1] = p
        
        player_dic[p] -= 1
        
    answer = [player_dic_rev[i] for i in range(len(players))]
    
    return answer