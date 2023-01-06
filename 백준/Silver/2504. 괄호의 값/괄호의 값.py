def operation(prev):
    if len(result)>0 and (result[-1] == "2)" or result[-1] == "3)"):
        if prev == ')' or prev == ']':
            result.append(")*(")          
        elif prev == '(' or prev == '[':
            result.append("+") 

parentInput = input()


stack = []
result = []
prev = None

for parent in parentInput:
    if parent == '(' or parent == '[':
        stack.append(parent)
        if len(result)>0 and (result[-1] == "2)" or result[-1] == "3)"):
            if prev == ')' or prev == ']':
                result.append("+") 
        result.append('(')         

    else:
        if len(stack) == 0:
            print(0)
            exit(0)
        st_pop = stack.pop()

        if (st_pop == '(' and parent == ')'):
            operation(prev)
            result.append("2)")
        elif (st_pop == '[' and parent == ']'):
            operation(prev)
            result.append("3)")
        
        # wrong input
        else:
            print(0)
            exit(0)
        prev = parent

sum = 0
try:
    sum = eval("".join(result))
    print(sum)
except:
    print(0)
    exit(0)
