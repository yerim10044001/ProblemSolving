import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, input().split())))

    for i in range(1, n):
        # left
        triangle[i][0] += triangle[i-1][0]
        # mid
        for j in range(1, i):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        # right
        triangle[i][i] += triangle[i-1][i-1]
    
    print(max(triangle[n-1]))