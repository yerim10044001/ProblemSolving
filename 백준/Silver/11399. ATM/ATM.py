import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    pList = list(map(int, input().split()))
    pList.sort()
    pSum = 0
    for i in range(0,n):
        pSum += (n-i)*pList[i]

    print(pSum)
