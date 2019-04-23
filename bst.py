from day_18 import Queue

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def __init__(self):
        self.queue = Queue()

    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root == None:
            return -1
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def levelOrder(self,root):
       queue = [] 
       if root != None:
            queue.append(root)
            while len(queue) > 0 :
                node = queue[0]
                del queue[0]
                print(node.data, end=" ")
               
                if node.left != None:
                    queue.append(node.left)
                
                if node.right != None:
                    queue.append(node.right)

T = [6,3,5,4,7,2,1]
myTree=Solution()
root=None
for data in T:
    root=myTree.insert(root,data)
myTree.levelOrder(root)