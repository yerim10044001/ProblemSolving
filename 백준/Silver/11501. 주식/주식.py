import sys
input = sys.stdin.readline

def getMaxProfit(stocks):
    stocks.reverse()
    maxStock = stocks[0]
    profit, temp = 0, 0
    cnt = 0
    
    for stock in stocks[1:]:
        if stock > maxStock:
            profit -= temp
            profit += cnt*maxStock
            maxStock = stock
            temp, cnt = 0, 0
        else:
            cnt += 1
            temp += stock

    profit -= temp
    profit += cnt*maxStock

    return profit

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        stocks = list(map(int, input().split()))
        print(getMaxProfit(stocks))
