
def solve(n, buildings):
    answer = 0
    for i in range(2, n-2):
        views = [buildings[i]-buildings[i-1],
                   buildings[i]-buildings[i-2],
                   buildings[i]-buildings[i+1],
                   buildings[i]-buildings[i+2]]
        if min(views) > 0:
            answer += min(views)
    return answer


if __name__ == '__main__':
    for t in range(1, 11):
        n = int(input())
        buildings = list(map(int, input().split()))
        answer = solve(n, buildings)
        print(f'#{t} {answer}')



