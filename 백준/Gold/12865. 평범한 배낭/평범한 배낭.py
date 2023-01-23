import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())

    stuffList = [(0,0)]
    bag = [[0 for _ in range(0, k+1)]]

    for _ in range(0, n):
        w, v = map(int, input().split())
        stuffList.append((w, v))

    # 물건 무게(w) 기준으로 정렬
    stuffList.sort(key= lambda x : x[0])

    #
    for i in range (1, n+1):
        subset = []
        for w in range(0, k+1):
            if stuffList[i][0] > w:
                subset.append(bag[i-1][w])
            else:
                subset.append(max(bag[i-1][w], stuffList[i][1]+ bag[i-1][w-stuffList[i][0]]))
        bag.append(subset)
        
    print(bag[n][k])