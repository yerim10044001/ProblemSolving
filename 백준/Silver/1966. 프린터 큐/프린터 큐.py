import sys
input = sys.stdin.readline

if __name__ == "__main__":
    k = int(input())

    for _ in range(0, k):
        n, m = map(int, input().split())
        queue = list(map(int, input().split()))

        count = 0

        while True:
            # pop 가능
            if queue[0] == max(queue):
                count += 1
                if m == 0:
                    print(count)
                    break
                queue.pop(0)
                m -= 1
            # pop 불가능
            else:
                if m == 0:
                    m = len(queue)-1
                else:
                    m -= 1
                queue = queue[1:]+[queue[0]]

