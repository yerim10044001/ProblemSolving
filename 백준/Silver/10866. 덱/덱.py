import sys
input = sys.stdin.readline

def processOrder(order):
    # push
    if "push" in order:
        order = order.split()
        if order[0] == "push_front":
            deque.insert(0, int(order[1]))
        elif order[0] == "push_back":
            deque.append(int(order[1]))
    # pop
    elif "pop" in order and len(deque) > 0:
        order = order.split()
        if order[0] == "pop_front":
            print(deque.pop(0))
        elif order[0] == "pop_back":
            print(deque.pop())
    elif "pop" in order and len(deque) == 0:
        print("-1")
    # size
    elif order == "size":
        print(len(deque))
    # empty
    elif order == "empty":
        if len(deque) > 0:
            print("0")
        else:
            print("1")
    # front
    elif "front" == order and len(deque)>0:
        print(deque[0])
    elif "front" == order and len(deque)==0:
        print("-1")
    # back
    elif "back" == order and len(deque)>0:
        print(deque[-1])
    elif "back" == order and len(deque)==0:
        print("-1")

if __name__ == "__main__":
    n = int(input())
    deque = []

    for _ in range(0, n):
        order = input().rstrip()
        
        processOrder(order)
