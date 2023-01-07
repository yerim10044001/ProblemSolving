n, m = input().split(" ")
n = int(n)
m = int(m)
cardList = list(map(int,input().split(" ")))

max = 0

for i in cardList:
    for j in cardList[cardList.index(i)+1:]:
        for k in cardList[cardList.index(j)+1:]:
            sum = i+j+k
            if sum <= m and sum > max:
                max = sum

print(max)