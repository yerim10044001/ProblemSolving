import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    stack = [0]
    answer = []
    i = 1
    for _ in range(n):
        k = int(input())
        
        while len(stack) > 0:
            if stack[-1] != k and i<= n:
                answer.append('+')
                stack.append(i)
                i += 1
            elif stack[-1] == k:
                answer.append('-')
                stack.pop(-1)
                break
            else:
                print("NO")
                exit(0)
    
    print(*answer, sep='\n')