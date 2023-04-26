import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    numList = [ int(input()) for _ in range(n) ]
    numList.sort(reverse=True)
    print(*numList, sep='\n')