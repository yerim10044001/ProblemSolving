import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    
    numList = list(map(int, input().split()))

    for i in range(1, n):
        numList[i] = max(numList[i-1]+numList[i], numList[i])
    
    print(max(numList))