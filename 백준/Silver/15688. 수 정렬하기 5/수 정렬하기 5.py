import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    input_list = [ int(input()) for _ in range(n) ]
    input_list.sort()
    print(*input_list, sep='\n')