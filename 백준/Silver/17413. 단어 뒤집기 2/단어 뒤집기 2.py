import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    
    word = []
    reverse = True
    for i in s:
        if i == '<':
            if reverse:
                word.reverse()
            print(''.join(word), end = '')
            word = ['<']
            reverse = False
        elif i == '>':
            if reverse:
                word.reverse()
            print(''.join(word), end = '>')
            word = []
            reverse = True
        elif i == ' ':
            if reverse:
                word.reverse()
            print(''.join(word), end = ' ')
            word = []
        else:
            word.append(i)
    
    if reverse:
        word.reverse()
    print(''.join(word))