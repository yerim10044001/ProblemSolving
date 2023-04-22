import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    wordset = set()
    for _ in range(n):
        wordset.add(input().rstrip())

    words = list(wordset)
    words.sort(key=lambda p: (len(p), p))

    print(*words, sep='\n')

