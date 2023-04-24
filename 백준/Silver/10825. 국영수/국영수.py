import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    scores = []
    for _ in range(n):
        name, kor, eng, mat = input().split()
        scores.append([name, int(kor), int(eng), int(mat)])
    
    scores.sort(key=lambda p: (-p[1], p[2], -p[3], p[0]))
    for i in range(n):
        print(scores[i][0])