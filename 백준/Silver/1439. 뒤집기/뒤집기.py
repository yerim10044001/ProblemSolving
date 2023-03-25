import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    zeroSplit = [i for i in s.split('0') if i != '']
    oneSplit = [i for i in s.split('1') if i != '']
    print(min(len(zeroSplit), len(oneSplit)))
