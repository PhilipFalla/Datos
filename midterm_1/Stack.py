
class Stack:
    def __init__(self, size: int): #Defining attributes (constructor).
        self.max = size #defining a max/size so we know when the stack is full.
        self.elements = [None] * size
        self.top = -1 #Using a top 'pointer' so operations are of constant time complexity.

    def __repr__(self): #Format/method for printing a Stack object.
        return f'Current stack: {self.elements} | Top: {self.top}'
    
    def push(self, val: str) -> None: #Method for adding elements to the stack.
        if self.top == self.max - 1: #Case for exceeding the Stack size.
            print('Stack overflow')
            return None
        
        self.top += 1
        self.elements[self.top] = val

    def pop(self) -> any: #Method for using and removing the top element of the stack.
        if self.top == -1: #Case for empty stack.
            print('Stack underflow')
            return None

        val = self.elements[self.top]
        self.elements[self.top] = None 
        self.top -= 1
        return val
    
    def peek(self) -> any: #Method for using without removing the top element of the stack.
        if self.top == -1: #Case for an empty stack.
            print('Stack underflow')
            return None

        return self.elements[self.top]
    
    def search(self, key) -> bool:
        for i in range(self.top + 1):  # Recorremos desde 0 hasta el top y no hasta el final
            if self.elements[i] == key:
                return True
        return False
