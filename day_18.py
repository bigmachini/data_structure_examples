'''

Welcome to Day 18! Today we're learning about Stacks and Queues. Check out the Tutorial tab for learning materials and an instructional video!

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards. Can you determine if a given string, , is a palindrome?

To solve this challenge, we must first take each character in , enqueue it in a queue, and also push that same character onto a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing, popping, and comparing each character until our containers are empty (a non-match means  isn't a palindrome).

Write the following declarations and implementations:

Two instance variables: one for your , and one for your .
A void pushCharacter(char ch) method that pushes a character onto a stack.
A void enqueueCharacter(char ch) method that enqueues a character in the  instance variable.
A char popCharacter() method that pops and returns the character at the top of the  instance variable.
A char dequeueCharacter() method that dequeues and returns the first character in the  instance variable.

'''
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def peek(self):
        check = self.isEmpty()
        if check == False:
            return self.stack[-1]
        else:
            return check
    
    def pop(self):
        check = self.isEmpty()
        if check == False:
            value = self.stack[-1]
            del self.stack[-1]
            return value
        else:
            return check

    def size(self):
        return len(self.stack)

    def displayStack(self):
        check = self.isEmpty()
        if check == False:
            return self.stack
        else:
            return check

    def isEmpty(self):
        if self.stack and len(self.stack) > 0:
            return False
        else:
           return 'Stack is empty' 


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        check = self.isEmpty()
        if not check:
            val = self.queue[0]
            del self.queue[0]
            return val
        else:
            return check
    
    def peek(self):
        check = self.isEmpty()
        if not check:
            return self.queue[0]
        else:
            return check

    def size(self):
        return len(self.queue)

    def displayQueue(self):
        check = self.isEmpty()
        if check == False:
            return self.queue
        else:
            return check

    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        else:
            return 'Queue is empty'
        


stack = Stack()

print('stack size: {}'.format(stack.size()))
stack.push(0)
print('stack size: {}'.format(stack.size()))
print('stack values: {}'.format(stack.displayStack()))
print('stack peek: {}'.format(stack.peek()))
stack.push(1)
print('stack size: {}'.format(stack.size()))
print('stack values: {}'.format(stack.displayStack()))
print('stack peek: {}'.format(stack.peek()))
stack.push(2)
print('stack size: {}'.format(stack.size()))
print('stack values: {}'.format(stack.displayStack()))
print('stack peek: {}'.format(stack.peek()))
print('stack pop: {}'.format(stack.pop()))
print('stack size: {}'.format(stack.size()))
print('stack values: {}'.format(stack.displayStack()))
print('stack pop: {}'.format(stack.pop()))
print('stack pop: {}'.format(stack.pop()))
print('stack pop: {}'.format(stack.pop()))
print('stack pop: {}'.format(stack.pop()))


queue = Queue()

print('queue size: {}'.format(queue.size()))
queue.push(0)
print('queue size: {}'.format(queue.size()))
print('queue values: {}'.format(queue.displayQueue()))
print('queue peek: {}'.format(queue.peek()))
queue.push(1)
print('queue size: {}'.format(queue.size()))
print('queue values: {}'.format(queue.displayQueue()))
print('queue peek: {}'.format(queue.peek()))
queue.push(2)
print('queue size: {}'.format(queue.size()))
print('queue values: {}'.format(queue.displayQueue()))
print('queue peek: {}'.format(queue.peek()))
print('queue pop: {}'.format(queue.pop()))
print('queue size: {}'.format(queue.size()))
print('queue values: {}'.format(queue.displayQueue()))
print('queue pop: {}'.format(queue.pop()))
print('queue pop: {}'.format(queue.pop()))
print('queue pop: {}'.format(queue.pop()))
print('queue pop: {}'.format(queue.pop()))
