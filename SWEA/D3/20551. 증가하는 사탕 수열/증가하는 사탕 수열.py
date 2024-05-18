def solve(a, b, c):
    # 불가능
    if a<1 or b<2 or c<3:
        return -1

    candy = 0
    if b >= c:
        candy += b - (c-1)
        b = c-1
    if a >= b:
        candy += a - (b-1)
    return candy


if __name__ == '__main__':
    t = int(input())
    for t_c in range(1, t + 1):
        a, b, c = map(int, input().split())
        answer = solve(a, b, c)
        print(f'#{t_c} {answer}')
