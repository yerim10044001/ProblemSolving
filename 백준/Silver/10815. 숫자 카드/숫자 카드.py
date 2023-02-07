import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    card = set(map(int, input().split()))

    m = int(input())
    findCard = list(map(int, input().split()))

    for i in findCard:
        if i in card:
            print("1", end= ' ')
        else:
            print("0", end= ' ')