import sys
input = sys.stdin.readline

def scheduling(schedule, n):
    pList = [0 for _ in range(0, n+1)]
    for s in schedule:
        endDay = s[0]-1+s[1]
        if endDay <= n and pList[endDay] < max(pList[:s[0]]) + s[2]:
            pList[endDay] = max(pList[:s[0]]) + s[2]
    
    return max(pList)


if __name__ == "__main__":
    n = int(input())
    schedule = []
    for i in range(1, n+1):
        t, p = map(int, input().split())
        schedule.append((i, t, p))
    
    # 상담 끝나는 날 기준 정렬
    schedule = sorted(schedule, key= lambda x : x[0]+x[1])

    # scheduling 시작
    print(scheduling(schedule, n))