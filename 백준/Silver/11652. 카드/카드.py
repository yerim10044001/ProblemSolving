import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    numDic = {}
    for _ in range(n):
        num = int(input())
        try:
            numDic[num] += 1
        except:
            numDic[num] = 1

    ans = max(numDic.values())
    ans = min(k for k, v in numDic.items() if v == ans)
    print(ans)