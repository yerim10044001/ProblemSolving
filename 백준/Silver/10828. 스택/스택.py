import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())    

    stack = []

    for _ in range(n):
        order = input()

        if "push" in order:
            order = order.split()
            stack.append(order[1])
        elif "top" in order:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        elif "size" in order:
            print(len(stack))
        elif "empty" in order:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif "pop" in order:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())