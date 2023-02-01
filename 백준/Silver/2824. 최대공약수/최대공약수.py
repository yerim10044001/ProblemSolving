import sys
input = sys.stdin.readline

def GCD(a, b):
    while(b):
        a, b = b, a%b
    return a

if __name__ == "__main__":
    n = int(input())
    aList = list(map(int, input().split()))

    m = int(input())
    bList = list(map(int, input().split()))

    a, b = 1, 1

    for i in aList:
        a *= i
    for j in bList:
        b *= j

    gcd = GCD(a, b)
    if gcd >= 1000000000:
        gcd = str(gcd)[-9:]

    print(gcd)


    