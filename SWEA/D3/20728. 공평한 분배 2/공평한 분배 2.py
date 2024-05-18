def solve(n, k, candies):
    candies.sort()
    m = 1000000000
    for i in range(0, n - k + 1):
        m = min(m, candies[i + k - 1] - candies[i])

    if n == k:
        m = candies[n-1] - candies[0]
    return m


if __name__ == '__main__':
    t = int(input())
    for c in range(1, t + 1):
        n, k = map(int, input().split())
        candies = list(map(int, input().split()))
        answer = solve(n, k, candies)
        print(f'#{c} {answer}')
