x =[1,2,3,43,4,2,3,4,52,21,4,5,2]
print(sorted(x))
x = "goddsd"
print(''.join(sorted(x)))
x = "this is kenya"
print(x.replace(' ', '%20'))
x = {'this': 1, "is" : 2, "kenya" : 3}
print(len(x))
x,y = 'aabccccccaa',[]

for i in x:
    if len(y) == 0:
        y.append([i,1])
    else:
        if y[-1][0] == i:
            y[-1][1] += 1
        else:
            y.append([i,1])

res = []
for i in y:
    i[1] = str(i[1])
    res.append(''.join(i))

print(''.join(res))

class Node:
    def __init__(self, data=None):
        self.next, self.data = None, data

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        x = self.head
        while x  is not None:
            print(x.data, end=' ')
            x  = x.next

    def getNode(self, position):
        x = self.head
        i = 0
        while x  is not None:
            if i == position:
                print("Node: {} ".format(x.data))
                return x            
            x  = x.next
            i += 1

    def length(self):
        length = 0
        while(self.head.next):
            length += 1
            self.head = self.head.next
        return length

    def insertStart(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
 
    
    def insertEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
     
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=node

 
    def insert(self, positon, data):

        i = 0
        if positon == 0:
            self.insertStart(data)
            return
        
        length =  self.length()
        if positon ==  length:
            self.insertEnd(data)
            return    

        if positon > length:
            print('Invalid position ')
            return   

        laste = self.head
        while(laste.next):

            if positon == i:
                node = Node(data)
                node.next = laste.head
                laste.head = node
            i += 1

list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3
       
list1.insertStart('Sun')
list1.insertEnd('Thu')
list1.insertEnd('Sat')
list1.getNode(5)
list1.print()
print('length: {}'.format(list1.length()))