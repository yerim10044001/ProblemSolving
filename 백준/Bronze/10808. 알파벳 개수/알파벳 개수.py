import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    alphabet = [0]*26
    for i in s:
        alphabet[ord(i)-ord('a')] += 1
    
    print(' '.join(list(map(str,alphabet))))
