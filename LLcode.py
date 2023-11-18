class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LL:
    def __init__(self):
        self.head = None
        self.tail= None
        self.length = 0


    #insert at the end of the list 
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail=new_node
        else:
            self.tail.next =new_node
            self.tail= new_node
        self.length +=1

    #print the valuse of LL 
    def print_values(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()


    #insert the element at the beginning or LL
    def prepend(self,value):
        new_node = Node(value)
        if new_node is Node:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    #insert function in LL
    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == self.length:
            self.append(value)
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index ==  0:
            new_node.next = self.head
            self.head= new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1
        return True
    
    #traversal of LL
    def trv(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

# Search method in LL
    def search(self, target):
        current_node = self.head
        while current_node is not None:
            if current_node.value == target:
                print("Number is present")
                return True  
            current_node = current_node.next
    # If the loop completes and the target is not found
        print("Number is not present")
        return False
    
    #get the value of the index
    def get(self, index):
        if index == -1:
            return self.tail.value
        elif index < -1 or index >= self.length:
            raise IndexError("Index out of bounds")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    #set the value
    def set_value(self, index, value):
            node_value = self.get(index)
            if node_value :
                node_value.value = value
                return True
            return False
    
    #pop_first node 
    def pop_first(self):
        if self.length == 0:
            return None
        pop_node = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            pop_node.next = None 
        self.length -= 1
        return pop_node
    
    #pop methon in LL
    def pop(self):
        if self.length == 0:
            return None
        pop_node = self.tail
        if self.length == 1 :
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1 
        return pop_node


    
custom = LL()
custom.append(10)
custom.append(14)
custom.append(14)
custom.append(16) 
custom.prepend(20)
custom.insert(0,20)
custom.insert(1,50)
custom.get(5)
print(custom.set_value(1,78))
custom.print_values()
custom.trv()
custom.search(10)
custom.pop_first()
custom.print_values()
