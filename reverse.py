# reverse string using stack data structure

from stack import Stack

stack = Stack()

def reverse(string):
    for letter in string:
        stack.push(letter)
    
    reversedstring = ''
    for _ in range(len(string)):
        reversedstring += stack.pop()
    
    return reversedstring

print(reverse('bahahha'))