str = input()
str = str.upper()

# make dictionary
alphabet_dic = {}
for i in str:
    if i not in alphabet_dic:
        alphabet_dic[i] = 1
    else:
        alphabet_dic[i] += 1

# get Max key
maxKey = "?"
maxValue = 0
for key, value in alphabet_dic.items():
    if value>maxValue:
        maxValue = value
        maxKey = key
    elif value == maxValue:
        maxKey = "?"

print(maxKey)