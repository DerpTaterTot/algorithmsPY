# basic stack structure

class Stack():
    def __init__(self) -> None:
        self.items = []
        
    def push(self, item): # push -> put item on the stack
        self.items.append(item)     
        
    def pop(self): # pop -> get the top (last) item on the stack
        return self.items.pop() 
        
    def peek(self): # peek -> look at the top (last) item on the stack 
        return self.items[-1]

    def get_stack(self): # get_stack -> look at whole stack
        return self.items
    
    def is_empty(self):
        return not self.items
    
