class Node:
    def __init__(self, value, next= None):
        self.data = value
        self.next = next
    
class Stack:
    def __init__(self, name):
        self.name = name
        self.top_item = None 
        self.limit = 1000
        self.size = 0
    def push(self, value):
        if self.size<self.limit:
            newnode = Node(value)
            newnode.next = self.top_item
            self.top_item = newnode
            self.size += 1 
        else:
            print("Stack is Full")
    
    def peek(self):
        if self.size:
            return self.top_item.data
    def pop(self):
        if self.size:
            d = self.top_item
            self.top_item = self.top_item.next
            self.size -= 1
            return d.data
        print("This stack is totally empty")
    def get_name(self):
        return self.name
    
    def print_items(self,n):
        s =[]
        if self.size>0:
            temp = self.top_item
            if self.size == n:
                while temp:
                    s.append(temp.data)
                    temp = temp.next
            else:
                t = n - self.size
                while t:
                    s.append('-')
                    t -= 1
                while temp:
                    s.append(temp.data)
                    temp = temp.next    
                
        else:
            for _i in range(n):
                s.append('-')           
        
        return s