import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # find all primes
    k = 1000
    primes = [True]*1001
    primes[0] = primes[1] = False
    p = 2    
    while p*p <= k:
        if primes[p]:
            primes[p*p::p] = [False] * ((k - p*p) // p + 1)            
        p += 1

    # get prime count
    n = int(input())
    numList = list(map(int, input().split()))
    answer = 0
    
    for num in numList:
        if primes[num]:
            answer += 1

    print(answer)