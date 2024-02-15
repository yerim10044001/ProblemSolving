def solution(book_time):
    # sort by start time
    book_time.sort(key=lambda x: x[0])
    
    rooms = []
    for book in book_time:
        start_HH, start_MM = map(int, book[0].split(':'))
        end_HH, end_MM = map(int, book[1].split(':'))
        
        # 기존에 존재하는 객실 사용 가능한지 확인
        can_use = False
        for i in range(len(rooms)):
            if rooms[i] <= start_HH*60 + start_MM:
                can_use = True
                rooms[i] = end_HH*60+end_MM+10
                break
                
        # 새 객실 추가
        if not can_use:
            rooms.append(end_HH*60+end_MM+10)

    return len(rooms)