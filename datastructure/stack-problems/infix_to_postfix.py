#create stack
class createStack():
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.top = -1
        self.temp = []
        self.output = []
#push operation
def push(stack,item):
    if(stack.top == stack.maxsize):
        print('stack is overflow')
        return
    stack.top += 1
    stack.temp.insert(stack.top,item)
#pop operation
def pop(stack):
    if(stack.top == -1):
        print('stack is underflow')
        return
    temp1 = stack.temp[stack.top]
    stack.top -= 1
    return temp1
# precedence of operators
def prec(sympol):
    if(sympol == '/' or sympol == '*'):
        return 3
    elif(sympol == '-' or sympol == '+'):
        return 2
    else:
        return 1


def conversion(stack,exp):
    for i in range(0,len(exp),1):
        if(exp[i].isalpha()):
            stack.output.append(exp[i])
        else:
            if(len(stack.temp) == 0 ):
                push(stack,exp[i])                
            elif(prec(stack.temp[stack.top]) >= prec(exp[i]) ):
                push(stack,exp[i])
            else:
                while(prec(stack.temp[stack.top]) < prec(exp[i]) and stack.top >= 0 ):
                    stack.output.append(pop(stack))
                push(stack,exp[i])

    if(stack.top >= 0):
        for i in range(stack.top,-1,-1):
            stack.output.append(pop(stack))
    
    for i in range(0,len(stack.output),1):
        print(stack.output[i], end = "")

obj = createStack(50)
expr = 'a+b'
conversion(obj,expr)