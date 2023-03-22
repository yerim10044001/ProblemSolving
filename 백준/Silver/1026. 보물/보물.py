import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))

    aList.sort(reverse=True)
    bList.sort()

    answer = 0
    for i in range(n):
        answer += aList[i]*bList[i]
    
    print(answer)