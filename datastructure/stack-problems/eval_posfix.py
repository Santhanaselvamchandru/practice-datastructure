class createStack():
    def __init__(self):
        self.top = -1
        self.output = [] 

# stack array is empty or not
def isEmpty(stack):
    return (len(stack.arr) == 0 )

# push operands in to stack
def push(stack,item):
    stack.top += 1
    stack.output.insert(stack.top,item)


# pop operands  from stack
def pop(stack):
    if(stack.top == -1):
        print('stack is underflow')
        return
    temp = stack.output[stack.top]
    stack.top -= 1
    return temp


def eval(stack,exp):
    for i in exp:
        # character is numbers or letters push in to stack
        if(i.isalnum()):
            push(stack,i)
        #character is operator perform kind of operation
        else:
            #pop top of the two elements
            ele2 = pop(stack)
            ele1 = pop(stack)
            ele = 0
            #perform operations
            if(i ==  '+'):
                ele = int(ele1) + int(ele2)
            elif(i == '-'):
                ele = int(ele1) - int(ele2)
            elif(i == '*'):
                ele = int(ele1) * int(ele2)
            elif(i ==  '/'):
                ele = int(ele1) / int(ele2)
            else:
                print('not valid expression')
            push(stack,str(ele))
    # show top value of the stack
    print(stack.output[stack.top])


s = createStack()
expression = '231*+9-'
eval(s,expression)