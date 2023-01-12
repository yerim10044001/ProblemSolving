import sys
input = sys.stdin.readline

def numbercheck() :
    global study
    for i in range(M) :
        book = int(input())
        number = list(map(int, input().split()))
        for j in range(book - 1) :
            if number[j] < number[j + 1] :
                study = False
                break
        if not study :
            break
            
N, M = map(int, input().split())
study = True

numbercheck()
print('Yes' if study else 'No')
