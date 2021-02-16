from stack import Stack

stack = Stack()

def convert_int_to_bin(num):
    while num > 0:              
        stack.push(num % 2)

        num //= 2  
    
    number = 0
    
    for i in range(len(stack.get_stack())):
        number += stack.get_stack()[i] * 10 ** i
    
    return number

print(convert_int_to_bin(12))
        

       