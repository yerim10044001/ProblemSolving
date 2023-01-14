import sys
input = sys.stdin.readline

def getBreakPoint(a, b, c):
    if c-b > 0:
        return a//(c-b)+1
    else:
        return -1

if __name__ == "__main__":
    a, b, c = list(map(int, input().split()))

    print(getBreakPoint(a, b, c))
