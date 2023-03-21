import sys
input = sys.stdin.readline

def getNumber(expression, i):
    number = []
    while  i < len(expression) and expression[i] != '+' and expression[i] != '-':
        number.append(expression[i])
        i += 1
    number = int(''.join(number))
    return number, i

if __name__ == "__main__":
    expression = input().rstrip()

    answer, i = 0, 0

    # first number always 'plus'
    number, i = getNumber(expression, i)
    answer += number

    # () start
    p = True

    while i < len(expression):
        # plus
        if p and expression[i] == '+': p = True
        # minus
        elif expression[i] == '-': p = False
        i += 1

        # in ( )
        if not p:
            number, i = getNumber(expression, i)
            answer -= number
        # not in ()
        else:
            number, i = getNumber(expression, i)
            answer += number

    print(answer)