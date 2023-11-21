class stack:
    def __init__(self):
        self.list=[]
 
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self,item):
        self.list.append(item)
        return "values is appended"
    
    def pop(self):
        if self.isEmpty():
            return "no element in stack"
        else:
            self.list.pop()
            return "values is poped"
    def peek(self):
        if self.isEmpty():
            return "no element in stack"
        else:
            return print(self.list[len(self.list)-1])
    
    def print_stack(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            for item in reversed(self.list):
                print(f"| {item} |")
        
    def delete(self):
        self.list = None

        
        
custom = stack()
custom.push(90)
custom.push(30)
custom.push(50)
custom.push(10)
custom.print_stack()
custom.pop()
custom.peek()
