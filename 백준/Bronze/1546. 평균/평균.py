import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    scoreList = list(map(int, input().split()))
    m = max(scoreList)

    print((sum(scoreList)/m)*100/n)