import sys
input = sys.stdin.readline

def numberSum(serial):
    s = 0
    for i in serial:
        if '0' <= i <= '9':
            s += int(i)
    return s

if __name__ == "__main__":
    n = int(input())
    serials = []
    for _ in range(n):
        serials.append(list(input().rstrip()))

    serials.sort(key= lambda p: (len(p), numberSum(p), ''.join(p)))

    for i in serials:
        print(''.join(i))