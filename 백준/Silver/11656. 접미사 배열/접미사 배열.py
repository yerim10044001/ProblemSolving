import sys
input = sys.stdin.readline

if __name__ == "__main__":
    word = input().rstrip()

    wordList = []
    for i in range(0, len(word)):
        wordList.append(word[i:])

    wordList.sort()

    for w in wordList:
        print(w)