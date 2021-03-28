class createStack():
    def __init__(self):
        self.top = -1
        self.arr = []
        self.out = []

def push(stack,item):
    stack.top += 1
    stack.arr.insert(stack.top,item)

def pop(stack):
    if (stack.top == -1):
        return ""
    temp = stack.arr[stack.top]
    stack.top -= 1
    return temp


def conversion(stack,exp):
    for i in range(len(exp)-1,-1,-1):
        if(exp[i].isalpha()):
            push(stack,exp[i])
        else:
            temp1 = str(pop(stack))
            temp2 = str(pop(stack))
            res = temp1 + "" + temp2 + "" + exp[i]
            stack.out.append(res)
    for i in range(0,len(stack.out),1):
        print(stack.out[i],end = "")

s = createStack()
exp = '*-A/BC-/AKL'
conversion(s,exp)