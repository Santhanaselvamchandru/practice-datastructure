# create stack
class createStack():
    def __init__(self):
        self.arr = []
        self.top = -1
    
# push in to stack
def push(stack,val):
    stack.top += 1
    stack.arr.insert(stack.top,val)

# pop top value of stack
def pop(stack):
    if(stack.top == -1):
        print('stack is underflow')
        return
    temp = stack.arr[stack.top]
    stack.top -= 1
    return temp

# reverse operation
def reverse(stack,item):
    for i in item:
        push(stack,i)
    # show reverse string
    for i in range(stack.top,-1,-1):
        print(stack.arr[i])

s = createStack()
string = 'Hello World'

reverse(s,string)