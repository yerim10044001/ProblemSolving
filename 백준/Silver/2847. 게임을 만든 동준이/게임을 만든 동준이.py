import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    levels = [ int(input()) for _ in range(n) ]
    levels.reverse()

    answer = 0
    prev = levels[0]
    for level in levels[1:]:
        temp = level - prev + 1
        if temp > 0:
            answer += temp 
            prev = level - temp
        else: prev = level
    
    print(answer)
