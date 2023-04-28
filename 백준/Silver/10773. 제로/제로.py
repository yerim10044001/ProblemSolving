import sys
input = sys.stdin.readline


if __name__ == "__main__":
    k = int(input())
    stack = []

    for _ in range(k):
        a = int(input())
        if a == 0:
            stack.pop()
        else:
            stack.append(a)
    
    print(sum(stack))