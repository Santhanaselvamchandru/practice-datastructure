# default operations on tree
class Tree():
    def __init__(self):
        self.data = None
        self.left = None
        self.right =None
# insertion
def insert(root,data):
    newnode = Tree()
    newnode.data = data
    newnode.left = None
    newnode.right = None
    if not root:
        root = newnode
        return root
    if root.left == None:
        root.left = insert(root.left,data)
    elif root.right == None:
        root.right = insert(root.right,data)
    else:
        root.left.left = insert(root.left.left ,data)
    return root
    


# show tree elements
def show(root,mes,dep):
    if root == None:
        return
    show(root.left,'root-left : ',root.data)
    print(dep,mes,' ',root.data)
    show(root.right,'root-right',root.data)          
        
        

def inst(root):
    root = insert(root,10)
    root = insert(root,20)
    root = insert(root,30)
    root = insert(root,40)
    root = insert(root,50)
    root = insert(root,60)
    root = insert(root,70)
    show(root,'root',root.data)

# insetruction
root = None
inst(root)