# Reverse queue
# Queue implement using singly linked list
class SLL():
    def __init__(self,data):
        self.data = data
        self.next = None
# create stack
class stack():
    def __init__(self):
        self.arr = list()
        self.top = -1
# stack push operation
def push(s,item):
    s.top += 1
    s.arr.insert(s.top,item)

#stack pop operation
def pop(s):
    if s.top == -1:
        return False
    self.top -= 1
    self.arr.pop()
     
# Queue creation
class Queue():
    def __init__(self):
        self.rear = self.front = None
    
    # Enqueue
    def Enqueue(self,item):
        temp = SLL(item)
        if self.rear == None:
            self.rear = self.front = temp
            return
        self.rear.next = temp
        self.rear = temp
    # Dequeue
    def Dequeue(self):
        if self.front == None:
            print('Empty Queue')
            return
        temp = self.front
        self.front = temp.next
        del temp
    # Show queue elements
    def show(self):
        if self.front == None:
            print("Empty Queue")
            return
        temp = self.front
        while not temp == None:
            print(temp.data,end =" ")
            temp = temp.next
        print(end= '\n')
    # reverse Operation
    def reverse(self):
        s = stack()
        temp = self.front
        while not temp == None:
            push(s,temp.data)
            temp = temp.next
        print('reverse queue ')
        for i in range(s.top,-1,-1):
            print(s.arr[i],end= " ")

    # Queue instructions
if __name__ == '__main__':
    q = Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.show()
    #q.Dequeue()
    #q.show()
    q.reverse()