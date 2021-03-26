#create stack
class createStack():
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.top = -1
        self.arr = []
#push operation
def push(stack,item):
    if(stack.top == stack.maxsize):
        print('stack is overflow')
        return
    stack.top += 1
    stack.arr.insert(stack.top,item)
#pop operation
def pop(stack):
    if(stack.top == -1):
        print('stack is underflow')
        return
    temp = stack.arr[stack.top]
    stack.top -= 1
    return temp
# display elements
def display(stack):
    if(stack.top == -1):
        print('stack is Empty')
        return
    for i in range(stack.top,-1,-1):
        print(pop(stack))

stac = createStack(5)
push(stac,1)
push(stac,2)
push(stac,3)
display(stac)