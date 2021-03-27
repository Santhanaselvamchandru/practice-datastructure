class createStack():
    def __init__(self):
        self.top = -1
        self.arr = []
def push(stack,item):
    stack.top += 1
    stack.arr.insert(stack.top,item)
# check neighbor
def neighbor(bracket):
    if(bracket == ')'):
        return '('
    elif( bracket == ']'):
        return '['
    else:
        return '{'

def pop(stack):
    if(stack.top == -1):
        print('stack is underflow')
        return
    temp = stack.arr[stack.top]
    stack.top -= 1
    return temp

def check_balanced(stack,val):
    for i in val:
        if (i == '(' or i == '[' or i == '{'):
            push(stack,i)
        elif ( i == ')' or i == ']' or i == '}'):
            if (stack.arr[stack.top] == neighbor(i)):
                pop(stack)
            else:
                break
        else:
            break
    
    if(stack.top == -1):
        print('valid parentheses')
    else:
        print('not valid parentheses')
            


s = createStack()
e = '({[]{}(})'
check_balanced(s,e)