from itertools import product


def solution(users, emoticons):
    arr = [10, 20, 30, 40]
    rates_arr = list(product(arr, repeat=len(emoticons)))
    
    answer = []
    for rates in rates_arr:
        members = 0
        total_sales = 0
        
        for user_rate, user_price in users:
            # 사용자 별 구매비용 계산
            user_purchase_price = 0
            for rate, emoticon in zip(rates, emoticons):
                if user_rate <= rate:
                    user_purchase_price += (100 - rate) * emoticon / 100
            # 이모티콘 플러스 가입 확인
            if user_purchase_price >= user_price:
                members += 1
            else:
                total_sales += user_purchase_price
        
        answer.append([members, total_sales])

    return sorted(answer, key= lambda x: (-x[0], -x[1]))[0]