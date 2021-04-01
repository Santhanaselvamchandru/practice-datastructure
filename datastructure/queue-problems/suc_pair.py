# successive pair elements
# input [1,2,3,4,5]    output '(1,2),(3,4)'
class createQueue():
    def __init__(self):
        self.queue = list()
        self.front = self.rear = -1

# add element function
def enqueue(q,item):
    if not q.queue:
        q.rear += 1
        q.front += 1
        q.queue.insert(q.rear,item)
        return
    q.rear += 1
    q.queue.insert(q.rear,item)

# delete element function
def dequeue(q):
    if not q.queue:
        print('Empty queue')
        return
    temp = q.queue[q.front]
    q.front += 1
    if q.front >= q.rear:
        q.front = q.rear = -1
    return temp

# display elements
def show(q,msg):
    if not q.queue:
        print('Empty queue')
        return 
    print(msg)
    for i in range(q.front,q.rear+1,1):
        print(q.queue[i],end=' ')
    print(end='\n')

# successive pair 
def succ(q):
    for i in range(q.front,round(q.rear/2)+1,1):
        if q.front == -1:
            break
        temp1 = dequeue(q)
        temp2 = dequeue(q)
        if(temp1 and temp2):
            print('(',temp1,',',temp2,')',end=" ")
# instruction
def instru(q):
    enqueue(q,1)
    enqueue(q,2)
    enqueue(q,3)
    enqueue(q,4)
    enqueue(q,5)
    enqueue(q,6)
    succ(q)


que = createQueue()
instru(que)