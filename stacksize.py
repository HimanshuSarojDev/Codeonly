class stackSize:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    def print_stack(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            for item in reversed(self.list):
                print(f"| {item} |")

    def isEmpty(self):
        return len(self.list) == 0

    def isFull(self):
        return len(self.list) == self.maxsize

    def push(self, item):
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(item)
            return "Element is appended"

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            self.list.pop()
            return "Element is popped"

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


custom = stackSize(5)
custom.push(10)
custom.push(20)
custom.push(30)
custom.push(5)
custom.push(90)
custom.print_stack()
