import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, c = map(int, input().split())
    numList = list(map(int, input().split()))
    temp = list(numList)
    numList.sort(key=lambda p: (-temp.count(p), temp.index(p)))
    print(*numList)