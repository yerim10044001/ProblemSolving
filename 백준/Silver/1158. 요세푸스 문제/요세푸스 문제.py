import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())

    circleList = [i for i in range(1, n+1)]
    result = "<"
    p = 0       # pointer
    for _ in range(0, n-1):
        p += k - 1
        if (p >= len(circleList)):
            p = p % len(circleList)

        result += str(circleList.pop(p))+", "
    
    # last element
    result += str(circleList.pop())+">"

    print(result)