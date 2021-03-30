#  Tower Of Honai using iteration

""" 
                     n = 3
                     i % n == 1 -- source and dest
                     i % n == 2 -- source and aux
                     i % n == 0 -- aux and dest 
        source                auxilary        destination
            |                    |               |
          --|--                  |               |                
        ----|----                |               |
    --------|--------            |               |

            |                    |               |
            |                    |               |                --> source and dest  iter(1) % n(3) == 1 
        ----|----                |               |
    --------|--------            |             --|--

            |                    |               |
            |                    |               |                --> source and aux  iter(2) % n(3) == 2 
            |                    |               |              
    --------|--------        ----|----         --|--

            |                    |               |
            |                    |               |                --> aux and dest  iter(3) % n(3) == 0 
            |                  --|--             |
    --------|--------        ----|----           |

            |                    |               |
            |                    |               |                --> source and dest iter(4) % n(3) == 1
            |                  --|--             |
            |                ----|----   --------|--------

            |                    |               |
            |                    |               |               --> source and aux  iter(5) % n(3) == 2
            |                    |               |
          --|--              ----|----   --------|--------

            |                    |               |
            |                    |               |               --> aux and dest  iter(6) % n(3) == 0
            |                    |           ----|----
          --|--                  |       --------|--------

            |                    |               |
            |                    |             --|--            
            |                    |           ----|----          --> source and dest iter(7) % n(3) == 1
            |                    |       --------|--------

"""
# create three pegs (source ,auxilary, destination)
class createPegs():
    def __init__(self,disk):
        self.source = disk
        self.aux = list()
        self.dest = list()

# push function
def push(arr,item):
    arr.append(item)
# pop function
def pop(arr):
    if not arr:
        print('Empty list')
        return 
    return arr.pop()
# move disks function
def moveDisk(From,To,char1,char2):
    if not To:
        item = pop(From)
        push(To,item)
        moves(item,char1,char2)
        return
    if not From:
        item = pop(To)
        push(From,item)
        moves(item,char2,char1)
        return
    if From and To:
        temp1 = pop(From) 
        temp2 = pop(To)
        if temp1 < temp2:
            push(To,temp2)
            push(To,temp1)
            moves(temp1,char1,char2) 
        else:
            push(From,temp1)
            push(From,temp2)
            moves(temp2,char2,char1)


# display moves
def moves(item,char1,char2):
    print('disk ',item,' move ',char1,' to ',char2)

# main function
def TOH(disks):
    N = pow(2,len(disks))
    pegs = createPegs(disks)
    n = len(disks)
   
    for i in range(1,N,1):
        print(i)
        # i % n == 1 source and dest
        if i % n == 1 :
            moveDisk(pegs.source,pegs.dest,'S','D')
        # i % n == 2 source and aux
        if i % n == 2 :
            moveDisk(pegs.source,pegs.aux,'S','A')
        # i % n == 1 aux and dest
        if i % n == 0 :
            moveDisk(pegs.aux,pegs.dest,'A','D')


# default initialization and function calls
disk = [3,2,1]
TOH(disk)

"""
            ----output----
    Move the disk 1 from 'S' to 'D'
    Move the disk 2 from 'S' to 'A'
    Move the disk 1 from 'D' to 'A'
    Move the disk 3 from 'S' to 'D'
    Move the disk 1 from 'A' to 'S'
    Move the disk 2 from 'A' to 'D'
    Move the disk 1 from 'S' to 'D'
"""