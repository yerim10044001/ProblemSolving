if __name__ == "__main__":
    n = int(input())
    inputList = []
    for _ in range(0, n):
        inputList.append(input())

    for word in inputList:
        wordList = word.split(" ")
        wordA = wordList[0]
        wordB = wordList[1]

        if sorted(wordA) == sorted(wordB):
            print(wordA+" & "+wordB+" are anagrams.")
           
        else:
            print(wordA+" & "+wordB+" are NOT anagrams.")
