import sys
from itertools import *
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = list(permutations([i for i in range(1,n+1)], m))
    for r in result:
        print(' '.join(list(map(str,r))))