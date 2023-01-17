import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())

    circleList = [i for i in range(1, n+1)]
    result = "<"
    p = 0
    while(len(circleList) != 0):
        p += k - 1
        while(p >= len(circleList)):
            p -= len(circleList)


        if(len(circleList) != 1):
            result += str(circleList.pop(p))+", "
        else:
            result += str(circleList.pop(p))+">"

    print(result)