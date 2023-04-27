import bisect
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        a, b = map(int,input().split())
        aList = list(map(int, input().split()))
        bList = list(map(int, input().split()))
        bList.sort()
        aCnt = 0
        
        for i in aList:
            aCnt += bisect.bisect_left(bList, i)
        
        print(aCnt)


