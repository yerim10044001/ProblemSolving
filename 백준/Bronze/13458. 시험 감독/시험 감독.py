import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b, c = map(int, input().split())
    
    answer = 0
    for i in range(n):
        if a[i] > b: # 부감독관 필요
            if (a[i]-b)%c != 0:
                answer += 1
            answer += (a[i]-b)//c
        answer += 1

    print(answer)
