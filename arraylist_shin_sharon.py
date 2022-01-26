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
        self._adjust_internal_array(self.logical_size + 1)
        self.array[self.logical_size] = value
        self.logical_size += 1
    
    def __str__(self):
        output = "["
        if self.logical_size > 0:
            for i in range(self.logical_size-1):
                if str(self.array[i]).isalpha() is True:
                    output += f"'{self.array[i]}'"
                    output += ","
                elif str(self.array[i]).isdigit() is True:
                    output += str(self.array[i])
                    output += ","
            if str(self.array[self.logical_size-1]).isdigit() is True:
                output += str(self.array[self.logical_size-1])
            else:
                output += f"'{self.array[self.logical_size-1]}'"
        output += "]"
        return output
    
    def extend(self,other):
        self._adjust_internal_array(self.logical_size+other.logical_size)
        if type(other) != type(ArrayList()):
            raise ValueError("not an array list")
        for i in range(other.logical_size):
            self.array[self.logical_size + i] = other.array[i]
        self.logical_size += other.logical_size
                
    def __len__(self):
        return self.logical_size
    
    def _adjust_index(self,index):
        if index < 0 and index > (0 - self.logical_size -1):
            index += (self.logical_size)
            return index
        elif index < (0 - self.logical_size):
            raise IndexError("index out of negative range")
        elif index > (self.logical_size-1):
            raise IndexError("index out of range")
        else:
            return index
    
    def _adjust_internal_array(self,capacity_required):
        counter = len(self.array)
        if capacity_required > len(self.array) or capacity_required < (len(self.array)//3):
            while capacity_required > counter:
                counter*=2
            while capacity_required < (counter//3):
                counter//=2
            if counter < 10:
                counter = 10
            temp = SimpleArray(counter)
            for i in range(self.logical_size):
                temp[i] = self.array[i]
            self.array = temp
        
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
        counter = 0
        for i in range(self.logical_size):
            if self.array[i] == value:
                counter += 1
        return counter != 0
    
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
            elif self.array[i] != value and i == self.logical_size-1:
                raise ValueError("no value in arraylist")
    
    def __eq__(self,other):
        counter = 0
        if type(other) != type(ArrayList()) or type(self) != type(ArrayList()):
            return False
        elif self.logical_size != other.logical_size:
            return False
        else:
            for i in range(self.logical_size):
                if self.array[i] != other.array[i]:
                    counter += 1
            return counter == 0
            
    def insert(self,index,value):
        capacity = len(self.array)
        index = self._adjust_index(index)
        if self.logical_size == capacity:
            capacity = self._adjust_internal_array(self.logical_size + 1)
        for i in range(self.logical_size - index+1):
            self.array[self.logical_size - i] = self.array[self.logical_size - 1 - i]
        self.array[index] = value
        self.logical_size +=1   
            
    
    def remove(self,index=None):
        index = self._adjust_index(index)
        removed = self.array[index]
        self._adjust_internal_array(self.logical_size - 1)
        for i in range(self.logical_size - index):
            self.array[index + i] = self.array[index + i + 1]
        self.logical_size -= 1   
        return removed
    
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
    my_list = ArrayList(0,1,2,3,4,5,6,7,8,9,10,11)
    one_list = ArrayList(8,9,10,11,12)
    
    
    
    
