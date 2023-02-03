import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    starList = [['*' for _ in range(0, n)] for _ in range(0, n)]

    k = 3
    while k <= n:
        for i in range(0, n, k):
            for j in range(0, n, k):
                for h in range(k//3, k//3+k//3):
                    for g in range(k//3, k//3+k//3):
                        starList[i+h][j+g] = ' '

        k *= 3

    # print star
    for i in range(0, n):
        print(''.join(starList[i]))