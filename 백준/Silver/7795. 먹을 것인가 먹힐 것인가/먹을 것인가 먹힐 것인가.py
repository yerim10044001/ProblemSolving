import sys
input = sys.stdin.readline

def binarySearch(a, bList):
    left, right = 0, len(bList)-1
    while left <= right:
        mid = (left+right)//2
        if bList[mid] >= a:
            right = mid-1
        elif bList[mid] < a:
            left = mid+1
    return left

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        a, b = map(int,input().split())
        aList = list(map(int, input().split()))
        bList = list(map(int, input().split()))
        aList.sort()
        bList.sort()
        aCnt = 0
        for a in aList:
            i = binarySearch(a, bList)
            aCnt += i
 
        print(aCnt)


