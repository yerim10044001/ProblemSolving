import sys
input = sys.stdin.readline

def fibonacci(num):
    if fiboList[num] != [0, 0]:
        return fiboList[num]
    else:
        fiboList[num] = [fibonacci(num-1)[0] + fibonacci(num-2)[0], fibonacci(num-1)[1] + fibonacci(num-2)[1]]
        return fiboList[num]

if __name__ == "__main__":
    n = int(input())

    fiboList = [[0, 0] for _ in range(0, 41)]
    fiboList[0] = [1, 0]
    fiboList[1] = [0, 1]

    for _ in range(0, n):
        num = int(input())
        result = fibonacci(num)
        print(result[0], result[1])

    