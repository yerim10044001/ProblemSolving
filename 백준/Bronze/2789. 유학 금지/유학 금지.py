str = input()

# alphabet list
abcList = [True for _ in range(0,26)]

cambridge = "CAMBRIDGE"
for i in cambridge:
    abcList[ord(i)-ord('A')] = False

# result
for i in str:
    if(abcList[ord(i)-ord('A')]):
        print(i, end="")
