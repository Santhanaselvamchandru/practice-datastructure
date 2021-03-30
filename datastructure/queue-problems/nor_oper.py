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
    show(q,'Enqueue operation')

# delete element function
def dequeue(q):
    if not q.queue:
        print('Empty queue')
        return
    q.front += 1
    show(q,'Dequeue operation')

# display elements
def show(q,msg):
    if not q.queue:
        print('Empty queue')
        return 
    print(msg)
    for i in range(q.front,q.rear+1,1):
        print(q.queue[i],end=' ')
    print(end='\n')
# instruction
def instru(q):
    ## insert Elements
    enqueue(q,10)
    enqueue(q,20)
    enqueue(q,30)
    enqueue(q,40)
    # delete Elements
    dequeue(q)
    dequeue(q)

que = createQueue()
instru(que)