import sys
input = sys.stdin.readline

if __name__ == "__main__":
    expression = input().rstrip()
    try:
        m = expression.index('-')
        answer = sum(list(map(int, expression[:m].split('+'))))
        expression = expression[m+1:].replace('-','+')
        answer -= sum(list(map(int, expression.split('+'))))

    except:
        answer = sum(list(map(int, expression.split('+'))))

    print(answer)