# balanced brackets question solved using stack data structure

from stack import Stack

stack = Stack()

open = ['(', '[', '{']
closed = [')', ']', '}']

def is_match(openp, closedp):
    index1 = open.index(openp)
    index2 = closed.index(closedp)
    
    return index1 == index2
        
def balanced(string):
    isBalanced = True
    for bracket in string:
        if bracket in open:
            stack.push(bracket)
        else:
            if stack.is_empty():
                isBalanced = True
            else:
                top = stack.pop()
                if not is_match(top, bracket):
                    isBalanced = False
                    
    return isBalanced and stack.is_empty()


