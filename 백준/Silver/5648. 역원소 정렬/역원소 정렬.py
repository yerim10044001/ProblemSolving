import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, *nums = input().split()
    while int(n) > len(nums):
        nums += input().split()
    
    intList = []
    for num in nums:
        n = list(num)
        n.reverse()
        intList.append(int(''.join(n)))
    
    intList.sort()
    for num in intList:
        print(num)