def solve(number, cnt):
    global answer
    answer = 0
    visited = set()

    def dfs(n):
        global answer
        if n == cnt:
            answer = max(answer, int("".join(number)))
        else:
            for i in range(len(number)-1):
                for j in range(i+1, len(number)):
                    number[i], number[j] = number[j], number[i]
                    # dfs(n + 1)
                    if (n, int("".join(number))) not in visited:
                        visited.add((n, int("".join(number))))
                        dfs(n + 1)
                    number[i], number[j] = number[j], number[i]

    dfs(0)
    return answer


if __name__ == '__main__':
    test_num = int(input())
    for t in range(1, test_num + 1):
        number, cnt = input().split()

        answer = solve(list(number), int(cnt))
        print(f'#{t} {answer}')
