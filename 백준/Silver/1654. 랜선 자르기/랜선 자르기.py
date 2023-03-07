import sys
input = sys.stdin.readline

if __name__ == "__main__":
    k, n = map(int, input().split())

    lines = []
    for _ in range(k):
        lines.append(int(input()))

    left = 1
    right = max(lines)
    result = 1
    while left <= right:
        
        s = (left+right)//2
        cnt = 0

        for i in lines:
            cnt += i//s
        
        if cnt < n:
            right = s-1
        else:
            left = s+1
            result = max(result, s)

    print(result)
