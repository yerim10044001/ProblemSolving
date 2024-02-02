def solution(data, ext, val_ext, sort_by):
    data_index = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    answer = []
    for d in data:
        if d[data_index[ext]] < val_ext:
            answer.append(d)

    answer.sort(key=lambda x:x[data_index[sort_by]])
    return answer