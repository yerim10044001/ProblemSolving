import sys
input = sys.stdin.readline

def decompress(str):
    stack = []
    length = 0
    prev = None
    for i in str:
        if i == '(':
            stack.append([prev, length -1])
            length = 0
        elif i == ')':
            st = stack.pop()
            length = int(st[0]) * length + st[1]
        else:
            prev = i
            length += 1
    
    return length

if __name__ == "__main__":
    inputStr = input().rstrip()

    print(decompress(inputStr))
