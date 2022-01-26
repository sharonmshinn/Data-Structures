class ArrayList:
    def __init__(self,*args):
        initial_capacity = 10
        while initial_capacity < len(args):
            initial_capacity *= 2
        self.array = SimpleArray(initial_capacity)
        for i in range(len(args)):
            self.array[i] = args[i]
        self.logical_size = len(args)
    
    def append(self,value):
        capacity = len(self.array)
        if self.logical_size == capacity:
            capacity = self._adjust_internal_array(self.logical_size + 1)
        self.array[self.logical_size] = value
        self.logical_size += 1
    
    def __str__(self):
        output = "["
        for i in range(self.logical_size-1):
                output += str(self.array[i])
                output += ","
        output += str(self.array[self.logical_size-1]) + "]"
        return output
    
    def extend(self,other):
        if type(other) != type(ArrayList()):
            raise ValueError("not an array list")
        capacity = len(self.array)
        if self.logical_size == capacity:
            capacity = self._adjust_internal_array(self.logical_size + other.logical_size)
        for i in range(other.logical_size):
            self.array[self.logical_size + i] = other.array[i]
        self.logical_size += other.logical_size
                
    def __len__(self):
        return self.logical_size
    
    def _adjust_index(self,index):
        if index < 0:
            index += (self.logical_size)
        elif index < (0 - self.logical_size):
            raise IndexError("index out of negative range")
        return index
    
    def _adjust_internal_array(self,capacity_required):   
            if capacity_required > self.logical_size:
                temp = SimpleArray(len(self.array)*2)
                for i in range(self.logical_size):
                    temp[i] = self.array[i]
                self.array = temp
            elif capacity_required < (self.logical_size//3):
                temp = SimpleArray(len(self.array)//3)
                for i in range(self.logical_size):
                    temp[i] = self.array[i]
                self.array = temp
            return self.array


        
    def __getitem__(self,index):
        index = self._adjust_index(index)
        if index > self.logical_size:
            raise IndexError("index out of range")
        else:
            return self.array[index]
    
    def __setitem__(self,index,value):
        index = self._adjust_index(index)
        if index <= self.logical_size:
            self.array[index] = value
    
    
    def __contains__(self,value):
        for i in range(self.logical_size):
            if self.array[i] == value:
                return True
            else:
                return False
    
    def count(self,value):
        counter = 0
        for i in range(self.logical_size):
            if self.array[i] == value:
                counter += 1
        return counter
    
    def index(self,value):
        for i in range(self.logical_size):
            if self.array[i] == value:
                return i
            elif self.array[i] != value and i > self.logical_size:
                raise ValueError("no value in arraylist")
    
    def __eq__(self,other):
        if type(other) != type(ArrayList()):
            return False
        for i in range(self.logical_size):
            for i in range(other.logical_size):
                if self.array[i] != other.array[i]:
                    return False
                else:
                    return True
    
    def insert(self,index,value):
        capacity = len(self.array)
        index = self._adjust_index(index)
        if self.logical_size == capacity:
            capacity = self._adjust_internal_array(self.logical_size + 1)
        for i in range(self.logical_size - index+1):
            self.array[self.logical_size - i] = self.array[self.logical_size - 1 - i]
        self.array[index] = value
        self.logical_size +=1   
        return self.array
            
    
    def remove(self,index=None):
        capacity = len(self.array)
        index = self._adjust_index(index)
        if self.logical_size < capacity:
            capacity = self._adjust_internal_array(self.logical_size - 1)
        for i in range(self.logical_size - index):
            self.array[index + i] = self.array[index + i + 1]
        self.logical_size -= 1   
        return self.array
    
    
    
class SimpleArray:
    def __init__(self,capacity,fillValue = None):
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self,index):
        return self.items[index]
    
    def __setitem__(self,index,newItem):
        self.items[index] = newItem

if __name__ == "__main__":
    my_list = ArrayList(1,2,3,4,5,6,7,8,9,10)
    print(my_list)
    not_array = ArrayList(1,2,3,4,5,6,7,8,9,10)
    print(not_array)
    my_list.extend(not_array)
    print(my_list)
