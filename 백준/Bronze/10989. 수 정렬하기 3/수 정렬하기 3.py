import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    inputlist = [ 0 for i in range(10001) ]
    
    for _ in range(n):
        inputlist[int(input())] += 1

    for i in range(10001):
        if inputlist[i] != 0:
            for j in range(inputlist[i]):
                print(i)