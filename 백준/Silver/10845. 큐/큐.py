import sys
input = sys.stdin.readline

def processOrder(order):
    # push
    if "push" in order:
        order = order.split()
        queue.append(int(order[1]))
    # pop
    elif order == "pop":
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
    # size
    elif order == "size":
        print(len(queue))
    # empty
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    # front
    elif order == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    # back
    elif order == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)


if __name__ == "__main__":
    n = int(input())
    queue = []

    for _ in range(0, n):
        order = input().rstrip()
        processOrder(order)

