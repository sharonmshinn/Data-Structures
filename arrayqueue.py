class Queue:
    def __init__(self):
        self.array = SimpleArray(10)
        self.front = 0
        self.back = 0
        self.logical_size = 0
    def enqueue(self,value):
        # are full???
        if self.logical_size > 0 and self.front == self.back:
            self._expand_array()
        self.array[self.back] = value
        self.back = (self.back+1) % len(self.array)
        self.logical_size += 1
    def dequeue(self):
        if self.logical_size == 0:
            raise EmptyError()
        return_val = self.array[self.front]
        self.front = (self.front+1) % len(self.array)
        self.logical_size -= 1
        if len(self.array) > 10 and self.logical_size*4 <= len(self.array):
            self._contract_array()
        return return_val
    def first(self):
        if self.logical_size == 0:
            raise EmptyError()
        return self.array[self.front]
    def __len__(self):
        return self.logical_size
    def is_empty(self):
        return self.logical_size == 0
    def _expand_array(self):
        new_array = SimpleArray(len(self.array)*2)
        new_array[0] = self.array[self.front]
        i = (self.front+1) % len(self.array)
        j = 1
        while i != self.front:
            new_array[j] = self.array[i]
            i = (i+1)%len(self.array)
            j += 1
        self.front = 0
        self.back = self.logical_size
        self.array = new_array
    def _contract_array(self):
        new_array = SimpleArray(len(self.array)//2)
        new_array[0] = self.array[self.front]
        i = (self.front+1) % len(self.array)
        j = 1
        while i != self.back:
            new_array[j] = self.array[i]
            i = (i+1)%len(self.array)
            j += 1
        self.front = 0
        self.back = self.logical_size
        self.array = new_array
    def __repr__(self):
        the_repr_values = []
        for i in range(self.logical_size):
            the_repr_values.append(repr(self.array[(self.front+i)%len(self.array)]))
        return f"[{', '.join(the_repr_values)}]" 

class EmptyError(Exception):
    pass

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
    my_queue = Queue()
    for i in range(10):
        my_queue.enqueue(i)
    for i in range(2):
        my_queue.dequeue()
    my_queue.enqueue("MY QUEEN!")
    print(my_queue)
    print(my_queue.array)
    for i in range(10):
        my_queue.enqueue(i)
    print(my_queue)
    print(my_queue.array)
    print(len(my_queue))
    for i in range(13):
        my_queue.dequeue()
    print(my_queue)
    print(my_queue.array)
    my_queue.dequeue()
    print(my_queue)
    print(my_queue.array)
