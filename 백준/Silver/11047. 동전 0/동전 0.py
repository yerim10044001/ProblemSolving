import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    coins.reverse()
    answer = 0
    for coin in coins:
        if k >= coin:
            answer += k // coin
            k %= coin
    
    print(answer)