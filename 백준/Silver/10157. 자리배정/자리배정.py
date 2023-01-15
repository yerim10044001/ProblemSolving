import sys
input = sys.stdin.readline

if __name__ == "__main__":
    col, row = map(int, input().split())
    k = int(input().rstrip())

    if k > col*row:
        print("0")
        exit(0)
    shell = 0
    shell_start = 1
    for i in range(1, min(col, row)//2+2):
        if row == 1 or col == 1:
            shell += row*col
        else:
            shell += 2*row + 2*col -4
        if k <= shell:   
            # 껍질에서 위치 찾기
            if row == 1:
                x = i + k - shell_start
                y = i
            elif k <= shell_start+row-1: # 왼쪽 벽
                x = i
                y = i + k - shell_start
            elif k <= shell_start+row-1+col-1: # 위쪽
                x = i + k - (shell_start+row-1)
                y = i + row-1
            elif k <= shell_start+row-1+col-1+row-1: # 오른쪽
                x = i + col-1
                y = i + row-1 - (k - (shell_start+row-1+col-1))
            else: # 아래쪽
                x = i + col-1 - (k - (shell_start+row-1+col-1+row-1))
                y = i
            print(x, y)
            exit(0)
        col -= 2
        row -= 2
        shell_start = shell+1

