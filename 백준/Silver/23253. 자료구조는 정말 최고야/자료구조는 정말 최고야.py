if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    # dummy가 내림차순이 아니면 나열 불가
    for i in range(0, m):
        input()     # 더미 안에 있는 책 수
        dummy = list(map(int, input().split()))
        if dummy != sorted(dummy, reverse=True):
            print("No")
            exit(0)
    
    print("Yes")

