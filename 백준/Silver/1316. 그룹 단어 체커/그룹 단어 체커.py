import sys
input = sys.stdin.readline

def groupCheck(word):
    alphabetList = [False for _ in range(0,26)]
    isGroup = True
    prev = None
    for i in word:
        if i == prev:
            continue
        elif alphabetList[ord(i)-ord('a')]:
            isGroup = False
            break
        else:
            alphabetList[ord(i)-ord('a')] = True
        prev = i
    return isGroup

if __name__ == "__main__":
    n = int(input())
    groupNum = 0
    for _ in range(0,n):
        word = input().rstrip()
        if groupCheck(word):
            groupNum += 1
    print(groupNum)
        