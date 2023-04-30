import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    points = [ list(map(int, input().split())) for _ in range(n) ]
    points.sort(key= lambda p: (p[0],p[1]))
    for i in range(n):
        print(points[i][0], points[i][1])