import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    answer = 1
    for i in range(1, n+1):
        answer *= i
    print(answer)