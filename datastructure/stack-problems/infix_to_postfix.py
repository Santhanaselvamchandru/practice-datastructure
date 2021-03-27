# create stack
class createStack():
    def __init__(self):
        self.top = -1
        self.arr = []
        self.output = [] 

# stack array is empty or not
def isEmpty(stack):
    return (len(stack.arr) == 0 )

# push operands in to stack
def push(stack,item):
    stack.top += 1
    stack.arr.insert(stack.top,item)


# pop operands  from stack
def pop(stack):
    if(stack.top == -1):
        print('stack is underflow')
        return
    temp = stack.arr[stack.top]
    stack.top -= 1
    return temp

# precedence of operator
def prec(sympol):
    if(sympol == '^'):
        return 4
    elif(sympol == '/' or sympol == '*'):
        return 3
    elif(sympol == '+' or sympol == '-'):
        return 2
    else:
        return 1
# convert infix to postfix
def conversion(stack,exp):
    for i in exp:
        if( i.isalnum()):
            stack.output.append(i)
        elif(i == '('):
            push(stack,i)
        elif(i == ')'):
            if(isEmpty(stack)):
                print('Expression is not valid')
                break
            else:
                while(not stack.arr[stack.top] == '(' and not isEmpty(stack)):
                    sym = pop(stack)
                    stack.output.append(sym)
                pop(stack)
        else:
            if(isEmpty(stack)):
                push(stack,i)
            elif(prec(stack.arr[stack.top]) <= prec(i)):
                push(stack,i)
            else:
                while(not prec(stack.arr[stack.top]) <= prec(i) and not isEmpty(stack)):
                    stack.output.append(pop(stack))
    if(not isEmpty(stack)):
        for i in range(stack.top,-1,-1):
            stack.output.append(pop(stack))

    # show postfix expression
    for i in range(0,len(stack.output),1):
        print(stack.output[i],end= "")


        
s = createStack()
expression = '(1+2)-(4-3)*(6/2)'
conversion(s,expression)