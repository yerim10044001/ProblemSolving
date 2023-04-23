import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    members = []
    for _ in range(n):
        age, name = input().split()
        members.append([int(age), name])
    members.sort(key=lambda p: p[0])

    for i in range(n):
        print(members[i][0], members[i][1])