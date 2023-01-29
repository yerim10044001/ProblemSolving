def operation(numbers, index, value, target):
    if index < len(numbers):
        cnt1 = operation(numbers, index+1,value+numbers[index], target)
        cnt2 = operation(numbers, index+1,value-numbers[index], target)
        return cnt1+cnt2
    elif value == target:
        return 1
    else:
        return 0


def solution(numbers, target):
    return operation(numbers, 0, 0, target)