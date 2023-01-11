if __name__ == "__main__":

    wordList = []
    for _ in range(0,5):
        inputString = list(input().rstrip())
        inputString += ['' for _ in range(0, 15)]
        wordList.append(inputString)

    for i in range(0,15):
        for j in range(0,5):
            print(wordList[j][i], end ="")