import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = 1
    for i in range(3):
        num *= int(input())

    num_count = [0 for _ in range(10)]
    for i in str(num):
        num_count[int(i)] += 1

    for i in num_count:
        print(i)