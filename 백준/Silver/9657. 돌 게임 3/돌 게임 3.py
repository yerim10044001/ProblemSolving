import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    if n%7 == 2 or n%7 ==0:
        print("CY")
    else:
        print("SK")