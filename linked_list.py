class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

    def __str__(self):
        output = "LL["
        if self.head != None:
            output += str(self.head.value)
            current_node = self.head.next
            while current_node != None:
                output += ","
                output += str(current_node.value)
                current_node = current_node.next   
        output += "]"
        return output

    def __len__(self):
        the_length = 0
        if self.head != None:
            the_length += 1
            current_node = self.head.next
            while current_node != None:
                the_length += 1
                current_node = current_node.next
        return the_length

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("index cannot be less than 0")
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
            if current_node is None:
                raise IndexError("linked list index out of range")
        if current_node is None:
                raise IndexError("linked list index out of range")
        return current_node.value

    def index(self, value):
        current_node = self.head
        index = 0
        while current_node.value != value:
            current_node = current_node.next
            index += 1
            if current_node == None:
                return None
        return index

    def pop(self, index = None):
        if index is None:
            index = self.__len__() - 1
        if index == 0:
            return_value = self.head.value
            self.head = self.head.next
            return return_value
        else:
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            return_value = current_node.next.value
            current_node.next = current_node.next.next
            return return_value
        
            
    
    
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append("a")
    my_list.append("b")
    my_list.append("c")
    my_list.append("d")
    print(my_list.pop(1))
    
