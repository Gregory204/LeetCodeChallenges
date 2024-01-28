# Design a stack that supports push, pop, top, and retrieving the
# minimum element in constant time.
'''
Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

class MinStack(object):

    def __init__(self):
        self.val = 0
        self.values = []

    def push(self, val):
        self.val = val
        self.values.append(val)
        return None

    def pop(self):
        self.values.pop(-3)
        return None

    def top(self):
        return max(self.values)

    def getMin(self):
        return min(self.values)
