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
        self.length = 0
    def print(self):
        x = self.head
        while x  is not None:
            print(x.data, end=' ')
            x  = x .next

    def lenght(self):
        self.length
        while(self.head.next):
            self.length += 1
            self.head = self.head.next

    def insertStart(self,data):
        node = Node(data)
        tmpNode = self.head
        self.head = node
        node.next = tmpNode
    
    def insertEnd(self, data):
        node = Node(data)
        self.next = node

 
    def insert(self, positon, data):
        node = Node(data)
        if positon == 0:
            self.insertStart(data)
        elif positon == self.length:
            self.insertEnd(data)
        else:
            i = 0
            while(self.head.next):
                i += 1
                if i == positon:
                    node.next = self.head.next
                    self.head.next = node

list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3
       
list1.insertStart('Sun')
list1.insertEnd('Thur')
list1.print()
list1.lenght()
print('length: {}'.format(list1.length))