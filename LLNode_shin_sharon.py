
class LLNode:
    
    def __init__(self,value,*args):
        self.value = value
        if len(args) == 0:
            self.next = None
        else:
            self.next = LLNode(*args)
        
    
    def append(self,value):
        if self.next is None:
            self.next = LLNode(value)
        else:
            self.next.append(value)
            
    
    def __str__(self):
        output = f"LLN[{self.value!r}]"
        if self.next is not None:
            output += "->"
            output += self.next.__str__()
        return output
    
    
    def __repr__(self):
        output = f"LLNode({self.value!r}"
        if self.next is not None:
            output += self.next._repr_helper()
        output += ")"
        return output
    
    
    def _repr_helper(self):
        output = f", {self.value!r}"
        if self.next is not None:
            output += self.next._repr_helper()
        return output
    
    
    def extend(self,other):
        if self.next is None:
            self.next = other
        else:
            self.next.extend(other)
            
    
    def __len__(self):
        if self.next is None:
            return 1
        else:
            return 1 + self.next.__len__()
       
    
    def _adjust_index(self,index):
        if index >= 0:
            return index
        if index < (0 - self.__len__()):
            raise IndexError("index out of negative range")
        else:
            return self.__len__() + index
    
    def __getitem__(self,index):
        index = self._adjust_index(index)
        if index == 0:
            return self.value
        elif index > 0 and self.next is None:
            raise IndexError("linked list index is out of range")
        else:
            return self.next.__getitem__(index - 1)
            
    
    def __setitem__(self,index,value):
        index = self._adjust_index(index)
        if index == 0:
            self.value = value
        elif index > 0 and self.next is None:
            raise IndexError("linked list index is out of range")
        else:
            return self.next.__setitem__(index - 1, value)
        
    
    def __contains__(self,value):
        if self.value == value:
            return True
        elif self.next is None and self.value != value:
            return False
        return self.next.__contains__(value)
    
        
    def count(self,value):
        if self.next is not None and self.value == value:
            return self.next.count(value) + 1
        elif self.next is not None and self.value != value:
            return self.next.count(value) + 0
        elif self.next is None and self.value == value:
            return 1
        elif self.next is None and self.value != value:
            return 0
        
        
    def index(self,value):
        index = 0
        if self.value == value:
            return index
        elif self.next is None and self.value != value:
            raise ValueError("value not in linked list")
        else:
            index += (self.next.index(value) + 1)
            return index
                   
        
    
    def __eq__(self,other):
        if type(self) is not type(other):
            return False
        if self.value != other.value:
            return False
        elif self.value == other.value:
            return self.next.__eq__(other.next)
        

    
    def get_node(self,index):
        index = self._adjust_index(index)
        if index == 0:
            return self
        elif index > 0 and self.next is None:
            raise IndexError("linked list index is out of range")
        else:
            return self.next.get_node(index - 1)
        
    def insert_after(self,index,value):
        index = self._adjust_index(index)
        if index == 0:
            new_node = LLNode(value)
            new_node.next = self.next
            self.next = new_node
        elif index > 0 and self.next is None:
            raise IndexError("linked list index is out of range")
        else:
            self.next.insert_after(index - 1, value)
        
    def remove_after(self,index):
        index = self._adjust_index(index)
        if index == 0:
            removed_value = self.next.value
            self.next = self.next.next
            return removed_value
        if index > 0 and self.next is None:
            raise IndexError("linked list index is out of range")
        elif index >= self.__len__() - 1:
            raise IndexError("cannot remove after end of linked list")
        else:
            self.next.remove_after(index - 1)

        
    

    

if __name__ == "__main__":
    # Testing code
    # Add your own tests!
    my_list = LLNode('a','b','c')
    print(my_list)
    print(my_list.__repr__())
    my_list.append('d')
    print(my_list)
    print(my_list.__repr__())
    second_list = LLNode('1','1','2')
    print(second_list)
    my_list.extend(second_list)
    print(my_list)
    print(my_list.__len__())
    
    
    
    
    
    
    
   
    
