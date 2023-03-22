import sys
input = sys.stdin.readline

if __name__ == "__main__":

    n = int(input())
    ropes = [ int(input()) for _ in range(n) ]
    ropes.sort()

    maxWeight = 0
    for i in range(n):
        maxWeight = max(maxWeight, ropes[i] * (n-i))

    print(maxWeight)