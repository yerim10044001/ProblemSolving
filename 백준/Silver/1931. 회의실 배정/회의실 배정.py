import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    schedule = []
    for _ in range(0, n):
        start, end = map(int, input().split())
        schedule.append((start, end))

    # 끝나는 시간 기준으로 정렬, 끝나는 시간이 같을 경우 시작시간 기준 정렬
    schedule.sort(key= lambda p: (p[1],p[0]))

    count = 0
    endTime = 0
    for s in schedule:
        if s[0] >= endTime:
            count += 1
            endTime = s[1]

    print(count)