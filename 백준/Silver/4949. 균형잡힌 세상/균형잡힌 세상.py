import sys
input = sys.stdin.readline

def checkParenthesis(sentence):
    stack = []
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif (i == ')' or i == ']') and len(stack) == 0:
            return False
        elif i == ')' and stack.pop() != '(':
            return False
        elif i == ']' and stack.pop() != '[':
            return False
    
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        # get sentence
        sentence = input().rstrip()
        while sentence[-1] != ".":
            sentence += input().rstrip()

        # if sentence is end, exit program
        if sentence == ".":
            break
        
        if checkParenthesis(sentence):
            print("yes")
        else:
            print("no")
