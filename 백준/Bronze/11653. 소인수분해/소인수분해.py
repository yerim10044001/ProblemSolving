n = int(input())

i = 2
while True:
    if n % i == 0:
        print(i)
        n = n//i
    else:
        i += 1
    if n == 1:
        break
