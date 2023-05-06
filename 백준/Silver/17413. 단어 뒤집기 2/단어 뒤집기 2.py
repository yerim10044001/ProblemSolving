import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    s = s.replace('<','!<').replace('>','>!').split('!')

    answer = ''
    for word in s:
        if '<' in word:
            answer += word
        else:
            answer += ' '.join([k[::-1] for k in word.split(' ')])

    print(answer)