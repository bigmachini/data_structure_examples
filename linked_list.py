class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        
class LinkedList: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        res = head
        if head != None:
            while(head.next != None):
                next_head = head.next
                if head.data == next_head.data: 
                    if next_head.next != None:
                        t = next_head.next
                        head.next = t
                    else:
                        head.next = None
                else:
                    head = next_head
        self.display(head)
            