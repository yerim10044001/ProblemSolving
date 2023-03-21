import sys
input = sys.stdin.readline

if __name__ == "__main__":
    expression = input().rstrip().split('-')

    answer = sum(list(map(int, expression[0].split('+'))))

    for expr in expression[1:]:
        answer -= sum(list(map(int, expr.split('+'))))

    print(answer)
