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
        next, data = None, data

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def print(self):
        x = self.head
        while x  is not None:
            print(x.data, end=' ')
            x  = x .next
            

    def insert(self, positon, data, head):
        node = Node(data)
        if positon == 0:
            tmpNode = head.next
            head = node
            node.next = tmpNode
            self.length += 1
        elif positon == self.length:
            self.next = node

        else:
            i = 0
            while(head.next):
                i += 1
                if i == positon:
                    node.next = head.next
                    head.next = node



        self.length += 1


list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.head.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.print()          