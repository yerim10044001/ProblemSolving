import sys
input = sys.stdin.readline

def printResult(divisorList, n):
    print(n, "= ", end ='')
    for i in divisorList:
        print(i, end ='')
        if i != divisorList[-1]:
            print(" + ", end ='')
        else:
            print()


if __name__ == "__main__":
    n = int(input())
    while(n != -1):
        d_list = [1]
        d_sum = 1
        for i in range(2, n//2 + 1):
            if n%i == 0:
                d_sum += i
                d_list.append(i)
        if d_sum == n:
            printResult(d_list, n)
        else:
            print(n, "is NOT perfect.")

        n = int(input())