# Queue implement using singly linked list
# Node creation
class SLL():
    def __init__(self,data):
        self.data = data
        self.next = None

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
    # Queue instructions
if __name__ == '__main__':
    q = Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.show()
    q.Dequeue()
    q.show()