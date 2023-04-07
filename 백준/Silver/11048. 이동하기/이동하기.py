import sys
input = sys.stdin.readline

def maxCandy():
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                miro[i][j] += miro[i][j-1]
            elif j == 0:
                miro[i][j] += miro[i-1][j]
            else:
                miro[i][j] += max(miro[i-1][j], miro[i][j-1], miro[i-1][j-1])

    return miro[n-1][m-1]
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    miro = [ list(map(int, input().split())) for _ in range(n) ]
    print(maxCandy())

