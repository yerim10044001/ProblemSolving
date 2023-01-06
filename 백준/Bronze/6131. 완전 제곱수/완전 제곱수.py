n = int(input())

count = 0
for b in range(1, 501):
    a = (b*b + n)**(1/2)
    if int(a)==a and a <= 500 and a >= b:
        count += 1

print(count)