class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    #append methon in CLL
    def apped(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length +=1

    #print the valuse of LL 
    def print_values(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()

    #Insert at the start
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

    #insert methon on CLL
    def insert(self,index, value):
        new_node = Node(value)
        if index>self.length or index < 0 :
            return print('out of index')
        if index ==0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                self.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            if self.head == None:
                self.head = new_node
                self.tail = new_node
                self.next = new_node
            else:
                self.tail.next = new_node
                new_node.next = self.head
                self.tail = new_node
        else:
            temp_node = new_node
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

        #Traversal of cuircular LL
    def tra(self):
        current = self.head
        while current is not None:
            print(current.value)
            if current == self.head:
                break
    
    def search(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                print('value is present')
                return True
            current = current.next  # Update current to the next node
        print('value is not present')
        return False

    def delete(self):
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0




new = CLL()
new.apped(10)
new.apped(30)
new.prepend(40)
new.insert(2,20)
print(new.head.value)
print(new.tail.value)
new.print_values()
new.search(10)
new.delete()
new.print_values()
new.prepend()
