def solution(bandage, health, attacks):
    
    prev = 0
    curr_health = health
    
    for attack_time, damage in attacks:
        # recovery per sec
        curr_health += (attack_time-prev-1)*bandage[1]
        
        # additional recovery
        curr_health += ((attack_time-prev-1)//bandage[0])*bandage[2]
        
        # check over health
        if curr_health > health:
            curr_health = health
        
        # get damage
        curr_health -= damage
        
        # dead
        if curr_health <= 0:
            return -1
        
        prev = attack_time
        
    return curr_health